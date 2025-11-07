import torch
print("CUDA available:", torch.cuda.is_available())          # True आना चाहिए
print("CUDA device count:", torch.cuda.device_count())        # कम से कम 1 होना चाहिए
print("CUDA current device:", torch.cuda.current_device())    # 0 या आपके GPU का इंडेक्स
print("Device name:", torch.cuda.get_device_name(0))          # आपका RTX 4050 आना चाहिए
