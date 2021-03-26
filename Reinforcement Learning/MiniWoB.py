import numpy as np

WIDTH = 160
HEIGHT = 210
X_OFS = 10
Y_OFS = 75


# obs = {'mysz': 'zielona', 'kufel': 'po piwie'}

vectorized = {'Robo': '666', 'Ania': '777', 'Piesek': 'kość'}
class MiniWoBCropper(vectorized.ObservationWrapper):
    def __init__(self, env, keep_text=False):
        super(MiniWoBCropper, self).__init__(env)
        self.keep_text = keep_text
    def _observation(self, observation_n):
        res = []
        for obs in observation_n:
            if obs is None:
                res.append(obs)
                continue
            img = obs['vision'][Y_OFS:Y_OFS+HEIGHT,
                                X_OFS:X_OFS+WIDTH, :]
            img = np.transpose(img, (2, 0, 1))
            if self.keep_text:
                t_fun = lambda d: d.get('instruction', '')
                text = " ".join(map(t_fun, obs.get('text', [{}])))
                res.append((img, text))
            else:
                res.append(img)
        return res



print(text)

