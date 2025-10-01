from expyriment import design, control, stimuli
# screen refresh every 0 - 16.67 msec (~17msec)
# exp.clock.wait(1000 stops execution for 1 sec; if the screen refresh is ~ 10msec, the result is 1.01 msec
exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

# fixation.present()
t0 = exp.clock.time
fixation.present()

# Edited section below

# draw(stims) # draw stimuli 
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)

# exp.clock.wait(1000)

# text.present()
t1 = exp.clock.time
fix_duration = (t1 - t0)/1000

# exp.clock.wait(1000)
t0 = exp.clock.time
text.present()
exp.clock.wait(1000)
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()