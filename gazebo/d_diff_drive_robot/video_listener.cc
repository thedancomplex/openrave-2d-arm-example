/*
 * Copyright 2012 Open Source Robotics Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/

#include <gazebo/transport/transport.hh>
#include <gazebo/msgs/msgs.hh>
#include <gazebo/gazebo.hh>

#include <iostream>


int i = 0;
/////////////////////////////////////////////////
// Function is called everytime a message is received.
//void cb(ConstWorldStatisticsPtr &_msg)
void cb(ConstImageStampedPtr &_msg)
{
  // Dump the message contents to stdout.
// char filename[256];

  size_t size;


  int ssize = sizeof(_msg->image().data()) - sizeof(_msg->image().data()) +
         _msg->image().data().size();

  printf("%i - %i - w: %i - h: %i \n\r",i++, ssize, _msg->image().width(), _msg->image().height());
// char filename[256];


  // Save frames
  /*if (this->save)
  {
    snprintf(filename, sizeof(filename), "click-%04d.ppm", this->frameno++);
    this->SaveFrame(filename);
  }*/
  // Save frames
  /*if (this->save)
  {
    snprintf(filename, sizeof(filename), "click-%04d.ppm", this->frameno++);
    this->SaveFrame(filename);
  }*/



}

/////////////////////////////////////////////////
int main(int _argc, char **_argv)
{
  // Load gazebo
  printf("%i",-1);
  gazebo::load(_argc, _argv);

  printf("%i",0);
  gazebo::run();

  printf("%i",1);
  // Create our node for communication
  gazebo::transport::NodePtr node(new gazebo::transport::Node());
  node->Init();

  printf("%i",2);
  // Listen to Gazebo world_stats topic
  gazebo::transport::SubscriberPtr sub = node->Subscribe("/gazebo/default/DiffDrive/d_diff_drive_robot/camera/link/camera/image", cb);

  printf("%i",3);
  // Busy wait loop...replace with your own code as needed.
  while (true)
    gazebo::common::Time::MSleep(100);

  // Make sure to shut everything down.
  gazebo::transport::fini();
}
