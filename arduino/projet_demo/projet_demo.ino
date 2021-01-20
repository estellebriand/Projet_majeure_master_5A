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
#include <std_msgs/Int32.h>
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
std_msgs::Int32 state_msg;
char cmd;

ros::Publisher starter("arduino/start", &start_msg);
ros::Publisher state("arduino/state", &state_msg);


void both_motor(int speed){
  //control both motor for forward, backward or stop
  Encoder_1.runSpeed(speed);
  Encoder_2.runSpeed(-speed);
}

void turn_right(void){
  //control motor: turn right
  Encoder_1.runSpeed(-100);
  Encoder_2.runSpeed(-200);
}

void turn_left(void){
  //control motor: turn left
  Encoder_1.runSpeed(200);
  Encoder_2.runSpeed(100);
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

void process(){
  switch(cmd)
    {
      case '0': //stop
      both_motor(0);
      Encoder_3.runSpeed(0);
      Motor_4.stop(); 
      break;
      case '1':
      both_motor(100); //forward
      break;
      case '2':
      turn_left(); //forward
      break;
      case '3':
      turn_right(); //forward
      break;
      case '4': //bras haut pince ouverte
      arm_up();
      delay(6000);
      open_claw();
      delay(6000);
      Motor_4.stop();
      break;
      case '5': //bras haut pince fermee
      arm_up();
      delay(6000);
      close_claw();
      delay(6000);
      Motor_4.stop();
      break;
      case '6': //bras bas pince ouvert
      arm_down();
      delay(6000);
      open_claw();
      delay(6000);
      Motor_4.stop();
      break;
      case '7': //bras bas pince fermee
      arm_down();
      delay(6000);
      open_claw();
      delay(6000);
      Motor_4.stop();
      break;
      
      default:
      break;
    }
}

void command_callback(const std_msgs::Int32& msg)
{

  if(msg.data == 0){
    cmd = '0';
  }
 
  if(msg.data ==1){
    cmd= '1';
    }
    
  if(msg.data ==2){
    cmd= '2';
    }
  if(msg.data ==3){
    cmd= '3';
    }
  if(msg.data ==4){
    cmd= '4';
    }
  if(msg.data ==5){
    cmd= '5';
    }
  if(msg.data ==6){
    cmd= '6';
    }
  if(msg.data ==7){
    cmd= '7';
    }

  state_msg.data = msg.data; 
  state.publish(&state_msg);
}

void obstacle_callback(const std_msgs::Bool& msg){
  if(msg.data){
    state_msg.data = 0;
    state.publish(&state_msg);
    cmd = '0';
  }
  
}
ros::Subscriber<std_msgs::Int32> command_sub("/command", &command_callback);
ros::Subscriber<std_msgs::Bool> obstacle_sub("/obstacle", &obstacle_callback);


void setup()
{

  nh.initNode();
  nh.advertise(state);
  nh.subscribe(command_sub);
  nh.subscribe(obstacle_sub);
  
  attachInterrupt(Encoder_1.getIntNum(), isr_process_encoder1, RISING);
  attachInterrupt(Encoder_2.getIntNum(), isr_process_encoder2, RISING);
  attachInterrupt(Encoder_3.getIntNum(), isr_process_encoder3, RISING);
  //Serial.begin(115200);
  
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
  /*
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
      //both_motor(50);
      command(state_msg);
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
  }*/
  process();
  Encoder_1.loop();
  Encoder_2.loop();
  Encoder_3.loop();
 
  nh.spinOnce();
  delay(200);
  /*
  Serial.print("Spped 1:");
  Serial.print(Encoder_1.getCurrentSpeed());
  Serial.print(" ,Spped 2:");
  Serial.println(Encoder_2.getCurrentSpeed());
 
  Serial.print(" ,CurPos 3:");
  Serial.println(Encoder_3.getCurPos());
  */
}
