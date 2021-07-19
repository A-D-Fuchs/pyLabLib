from ..generic import camera


class IMAQdxCameraThread(camera.GenericCameraThread):
    """
    Generic IMAQdx camera device thread.

    See :class:`.camera.GenericCameraThread`.
    """
    parameter_variables=camera.GenericCameraThread.parameter_variables|{"detector_size","roi_limits","roi","buffer_size"}
    def connect_device(self):
        with self.using_devclass("IMAQdx.IMAQdxCamera",host=self.remote) as cls:
            self.device=cls(path=self.path)
    def _estimate_buffers_num(self):
        return self.min_buffer_size[1]
    def setup_task(self, path, remote=None, misc=None):
        self.path=path
        super().setup_task(remote=remote,misc=misc)


class EthernetIMAQdxCameraThread(IMAQdxCameraThread):
    """
    Generic Ethernet IMAQdx camera device thread.

    See :class:`.camera.GenericCameraThread`.
    """
    def connect_device(self):
        with self.using_devclass("IMAQdx.EthernetIMAQdxCamera",host=self.remote) as cls:
            self.device=cls(path=self.path)