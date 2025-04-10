# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Callbacks that run at each training loop :class:`.Event`.

Each callback inherits from the :class:`.Callback` base class. See detailed description and
examples for writing your own callbacks at the :class:`.Callback` base class.
"""
from composer.callbacks.activation_monitor import ActivationMonitor
from composer.callbacks.checkpoint_saver import CheckpointSaver
from composer.callbacks.early_stopper import EarlyStopper
from composer.callbacks.export_for_inference import ExportForInferenceCallback
from composer.callbacks.free_outputs import FreeOutputs
from composer.callbacks.health_checker import HealthChecker
from composer.callbacks.image_visualizer import ImageVisualizer
from composer.callbacks.lr_monitor import LRMonitor
from composer.callbacks.memory_monitor import MemoryMonitor
from composer.callbacks.mlperf import MLPerfCallback
from composer.callbacks.nan_monitor import NaNMonitor
from composer.callbacks.optimizer_monitor import OptimizerMonitor
from composer.callbacks.runtime_estimator import RuntimeEstimator
from composer.callbacks.speed_monitor import SpeedMonitor
from composer.callbacks.system_metrics_monitor import SystemMetricsMonitor
from composer.callbacks.threshold_stopper import ThresholdStopper

# Conditionally import eval_output_logging_callback
try:
    from composer.callbacks.eval_output_logging_callback import EvalOutputLogging
except ImportError:
    # Create a dummy class to avoid import errors
    class EvalOutputLogging:
        """Dummy class for when transformers is not available."""
        pass

# Conditionally import generate
try:
    from composer.callbacks.generate import Generate
except ImportError:
    # Create a dummy class to avoid import errors
    class Generate:
        """Dummy class for when transformers is not available."""
        pass

__all__ = [
    'ActivationMonitor',
    'OptimizerMonitor',
    'LRMonitor',
    'MemoryMonitor',
    'NaNMonitor',
    'SpeedMonitor',
    'CheckpointSaver',
    'MLPerfCallback',
    'EarlyStopper',
    'EvalOutputLogging',
    'ExportForInferenceCallback',
    'ThresholdStopper',
    'ImageVisualizer',
    'HealthChecker',
    'RuntimeEstimator',
    'SystemMetricsMonitor',
    'Generate',
    'FreeOutputs',
]
