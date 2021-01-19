/*
 
 * Function List:
 *    1. uint8_t MeEncoderOnBoard::getPortB(void);
 *    2. uint8_t MeEncoderOnBoard::getIntNum(void);
 *    3. void MeEncoderOnBoard::pulsePosPlus(void);
 *    4. void MeEncoderOnBoard::pulsePosMinus(void);
 *    5. void MeEncoderOnBoard::setMotorPwm(int pwm);
 *    6. double MeEncoderOnBoard::getCurrentSpeed(void);
 *    7. void MeEncoderOnBoard::updateSpeed(void);
 *
 
 */

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Bool.h>
#include <MeMegaPi.h>

MeEncoderOnBoard Encoder_1(PORT1); //moteur droit
MeEncoderOnBoard Encoder_2(PORT2); //moteur gauche
MeEncoderOnBoard Encoder_3(PORT3); //Pince hauteur
MeMegaPiDCMotor Motor_4(PORT4); //Pince

void isr_process_encoder1(void)
{
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    Encoder_1.pulsePosMinus();
  }
  else
  {
    Encoder_1.pulsePosPlus();;
  }
}

void isr_process_encoder2(void)
{
  if(digitalRead(Encoder_2.getPortB()) == 0)
  {
    Encoder_2.pulsePosMinus();
  }
  else
  {
    Encoder_2.pulsePosPlus();
  }
}

void isr_process_encoder3(void)
{
  if(digitalRead(Encoder_3.getPortB()) == 0)
  {
    Encoder_3.pulsePosMinus();
  }
  else
  {
    Encoder_3.pulsePosPlus();
  }
}

/*=================ROS=================*/
//creation du ros node
ros::NodeHandle  nh;

std_msgs::Bool start_msg;
std_msgs::String state_msg;

ros::Publisher starter("arduino/start", &start_msg);
ros::Publisher state("arduino/state", &state_msg);


void both_motor(int speed){
  //control both motor for forward, backward or stop
  Encoder_1.runSpeed(speed);
  Encoder_2.runSpeed(-speed);
}

void turn_right(void){
  //control motor: turn right
  Encoder_1.runSpeed(0);
  Encoder_2.runSpeed(-200);
}

void turn_left(void){
  //control motor: turn left
  Encoder_1.runSpeed(200);
  Encoder_2.runSpeed(0);
}

void arm_up(void){
  Encoder_3.moveTo(0,50);
}

void arm_down(void){
  Encoder_3.moveTo(700,50);
}

void close_claw(void){
  Motor_4.run(-50);
}

void open_claw(void){
  Motor_4.run(50);
}
void command_callback(const std_msgs::String& data){
  state_msg.data = data.data;
  state.publish(&state_msg);
  if(data.data == "Stop"){
    both_motor(0);
  }
   else if("Forward"){
    both_motor(50);
    }

}

ros::Subscriber<std_msgs::String> command_sub("/command", command_callback);


void setup()
{

  nh.initNode();
  nh.advertise(state);
  nh.subscribe(command_sub);
  
  attachInterrupt(Encoder_1.getIntNum(), isr_process_encoder1, RISING);
  attachInterrupt(Encoder_2.getIntNum(), isr_process_encoder2, RISING);
  attachInterrupt(Encoder_3.getIntNum(), isr_process_encoder3, RISING);
  Serial.begin(115200);
  
  //Set PWM 8KHz
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);

  // For driving motor
  Encoder_1.setPulse(7);
  Encoder_2.setPulse(7);
  Encoder_1.setRatio(26.9);
  Encoder_2.setRatio(26.9);
  Encoder_1.setPosPid(1.8,0,1.2);
  Encoder_2.setPosPid(1.8,0,1.2);
  Encoder_1.setSpeedPid(0.18,0,0);
  Encoder_2.setSpeedPid(0.18,0,0);

  // for arm
  Encoder_3.setPulse(8);
  Encoder_3.setRatio(46.67);
  Encoder_3.setPosPid(1.8,0,1.2);
  Encoder_3.setSpeedPid(0.18,0,0);
  }

void loop()
{
  //nh.spinOnce();
  //delay(1000);

  if(Serial.available())
  {
    char a = Serial.read();
    switch(a)
    {
      case '0':
      both_motor(0);
      Encoder_3.runSpeed(0);
      Motor_4.stop();
      break;
      case '1':
      both_motor(50);
      break;
      case '2':
      turn_right();
      break;
      case '3':
      turn_left();
      break;
      case '4':
      arm_up();
      break;
      case '5':
      arm_down();
      break;
      case '6':
      close_claw();
      delay(6000);
      open_claw();
      delay(6000);
      Motor_4.stop();
      break;
      case '7':
      open_claw();
      break;
      
      default:
      break;
    }
  }
  Encoder_1.loop();
  Encoder_2.loop();
  Encoder_3.loop();
  /*
  Serial.print("Spped 1:");
  Serial.print(Encoder_1.getCurrentSpeed());
  Serial.print(" ,Spped 2:");
  Serial.println(Encoder_2.getCurrentSpeed());
  
  Serial.print(" ,CurPos 3:");
  Serial.println(Encoder_3.getCurPos());
  */
}
