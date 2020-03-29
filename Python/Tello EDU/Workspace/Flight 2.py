#coding:utf-8
import tello
import time

drone = tello.Tello('192.168.10.2', 8888)
print 'Battery:%s%%' % drone.get_battery()

drone.takeoff()
time.sleep(1)

drone.set_speed(2.2)
time.sleep(1)

drone.move_up(3)
time.sleep(1)

print 'rotate_cw',drone.rotate_cw(180)
time.sleep(1)
print 'move_forward',drone.move_forward(6)
time.sleep(1)
print 'flip',drone.flip(f)
time.sleep(1)
print 'move_forward',drone.move_forward(6)
time.sleep(1)

print 'rotate_ccw',drone.rotate_ccw(180)
time.sleep(1)
print 'move_forward',drone.move_forward(6)
time.sleep(1)
print 'flip',drone.flip(f)
time.sleep(1)
print 'move_forward',drone.move_forward(6)
time.sleep(1)


print 'move_forward',drone.move_left(4)
time.sleep(1)

print 'rotate_cw',drone.rotate_cw(180)
time.sleep(1)
print 'move_forward',drone.move_forward(12)
time.sleep(1)

print 'rotate_ccw',drone.rotate_ccw(180)
time.sleep(1)
print 'move_forward',drone.move_forward(12)
time.sleep(1)

print 'move_forward',drone.move_right(4)
time.sleep(1)

print 'drone.land',drone.land()

print 'Battery:%s%%' % drone.get_battery()
print 'Flight time: %s' % drone.get_flight_time()
