import os
import sys

import win32com.client

def installWindowsTask():
    scheduler = win32com.client.Dispatch(dispatch='Schedule.Service')
    scheduler.Connect()
    task = scheduler.NewTask(flags=0)
    task.RegistrationInfo.Author = 'Alexandros Ntigkaris'
    task.RegistrationInfo.Description = 'Runs cerberus.py file daily every one hour'
    task.RegistrationInfo.URI = 'cerberus'
    trigger = task.Triggers.Create(Type=2)
    trigger.Repetition.Interval = 'PT1H'
    trigger.Repetition.Duration = 'P1D'
    trigger.Repetition.StopAtDurationEnd = True
    trigger.StartBoundary = '1900-01-01T00:00:00'
    trigger.ExecutionTimeLimit = 'PT30M'
    trigger.Enabled = True
    task.Settings.DisallowStartIfOnBatteries = False
    task.Settings.StopIfGoingOnBatteries = False
    task.Settings.AllowHardTerminate = True
    task.Settings.StartWhenAvailable = False
    task.Settings.RunOnlyIfNetworkAvailable = False
    task.Settings.IdleSettings.StopOnIdleEnd = False
    task.Settings.IdleSettings.RestartOnIdle = False
    task.Settings.Enabled = True
    task.Settings.Hidden = False
    task.Settings.RunOnlyIfIdle = False
    task.Settings.WakeToRun = False
    task.Settings.ExecutionTimeLimit = 'PT1H'
    task.Settings.Priority = 7
    action = task.Actions.Create(Type=0)
    action.Path = sys.executable.replace('python','pythonw')
    action.Arguments ='cerberus.py'
    action.WorkingDirectory = f'{os.getcwd()}\\src'
    scheduler.GetFolder('\\')\
            .RegisterTaskDefinition(Path='cerberus',
                                    pDefinition=task,
                                    flags=6,
                                    UserId='',
                                    password='',
                                    LogonType=0)

if __name__=='__main__':
    installWindowsTask()
