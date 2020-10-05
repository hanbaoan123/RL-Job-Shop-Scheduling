from typing import Dict
from ray.rllib.agents.callbacks import DefaultCallbacks
from ray.rllib.env import BaseEnv
from ray.rllib.evaluation import MultiAgentEpisode, RolloutWorker
from ray.rllib.policy import Policy
from ray.rllib.utils.typing import PolicyID


class CustomCallbacks(DefaultCallbacks):
    
    def __init__(self, legacy_callbacks_dict: Dict[str, callable] = None):
        super(CustomCallbacks, self).__init__(legacy_callbacks_dict)
        self.best_time_step = float('inf')
        self.best_actions = []

    def on_episode_end(self, worker: "RolloutWorker", base_env: BaseEnv,
                       policies: Dict[PolicyID, Policy],
                       episode: MultiAgentEpisode, **kwargs):
        env = base_env.get_unwrapped()[0]
        episode.custom_metrics['time_step'] = env.current_time_step


