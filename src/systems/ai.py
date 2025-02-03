def step_ai(state, graphics, audio):
    for e in state.stage.entities:
        if e.ai:
            e.ai.step(e, state, graphics, audio)
