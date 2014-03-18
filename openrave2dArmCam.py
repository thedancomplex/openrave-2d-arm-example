#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Daniel M. Lofaro (dan@danlofaro.com)
# Modified from 2009-2011 Rosen Diankov (rosen.diankov@gmail.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Shows how to use the TranslationXY2D planar translation inverse kinematics type for an arm with few joints.

.. examplepre-block:: tutorial_iktranslation2d

.. examplepost-block:: tutorial_iktranslation2d
"""
from __future__ import with_statement # for python 2.5
__author__ = 'Daniel M. Lofaro'

from PyQt4 import QtCore, QtGui
import time
import openravepy
import numpy as np
if not __openravepy_build_doc__:
    from openravepy import *
    from numpy import *



def main(env,options):
    "Main example code."
    env.Load(options.scene)
    robot = env.GetRobots()[0]
    if options.manipname is not None:
        robot.SetActiveManipulator(options.manipname)

    sensors = env.GetSensors()
    ienablesensor = 0
    for i,sensor in enumerate(sensors):
        if i==ienablesensor:
            sensor.Configure(Sensor.ConfigureCommand.PowerOn)
            sensor.Configure(Sensor.ConfigureCommand.RenderDataOn)
        else:
            sensor.Configure(Sensor.ConfigureCommand.PowerOff)
            sensor.Configure(Sensor.ConfigureCommand.RenderDataOff)
        print 'showing sensor %s, !!!'%(sensors[ienablesensor].GetName())


# generate the ik solver
    ikmodel = databases.inversekinematics.InverseKinematicsModel(robot, iktype=IkParameterization.Type.TranslationXY2D)
    if not ikmodel.load():
        ikmodel.autogenerate()



    data = sensor.GetSensorData()

#    data = array(robot.GetAttachedSensors()[0].GetData().imagedata)
    while True:
        with env:
#            robot.GetAttachedSensors()[0].GetData().imagedata
            d = [0,np.random.normal(),0]
            robot.SetDOFValues(d,ikmodel.manip.GetArmIndices())
            env.UpdatePublishedBodies()
            time.sleep(0.1)
        h=None

from optparse import OptionParser
from openravepy.misc import OpenRAVEGlobalArguments

@openravepy.with_destroy
def run(args=None):
    """Command-line execution of the example.

    :param args: arguments for script to parse, if not specified will use sys.argv
    """
    parser = OptionParser(description='Shows how to use different IK solutions for arms with few joints.')
    OpenRAVEGlobalArguments.addOptions(parser)
    parser.add_option('--scene',action="store",type='string',dest='scene',default='tridoftable.env.xml',
                      help='Scene file to load (default=%default)')
    parser.add_option('--manipname',action="store",type='string',dest='manipname',default=None,
                      help='name of manipulator to use (default=%default)')
    (options, leftargs) = parser.parse_args(args=args)
    OpenRAVEGlobalArguments.parseAndCreateThreadedUser(options,main,defaultviewer=True)

if __name__ == "__main__":
    run()
