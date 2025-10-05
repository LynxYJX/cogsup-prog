from expyriment import design, control, stimuli
import random

def load(stims):
    # preload the stimuli passed as input
    for stim in stims:
        stim.preload()

def timed_draw(stims):
    # return the time it took to draw
    # draw a list of (preloaded) stimuli on-screen, return the time it took to execute the drawing
    t0 = exp.clock.time
    # Clear the back buffer
    exp.screen.clear()
    # Draw stimuli to the back buffer
    if stims:
        for stim in stims:
            stim.present(clear=False, update=False)
    # Update the screen to show the stimuli
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0
def present_for(stims, t=1000):
    # draw and keep stimuli on-screen for time t in ms (be mindful of edge cases!)
    # Clear the back buffer and draw the first stimulus
    draw_time = timed_draw(stims)
    wait_time = t - draw_time
    if wait_time > 0:
        exp.clock.wait(wait_time)


""" Test functions """
exp = design.Experiment()
control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()
