from expyriment import design, control, stimuli
# 1: Global Setting
exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

# 2: Stimuli
fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

# 3: Experiment Execution
control.start(subject_id=1)

# Present the fixation cross by itself
fixation.present(clear=True, update=True)
exp.clock.wait(500)

# Clear the back buffer and draw the fixation cross onto it
fixation.present(clear=True, update = False) # Added line 
# Draw the square onto the same back buffer
square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()
