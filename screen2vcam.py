import argparse
import cv2          # [opencv-python]   v4.5.4.58+
import mss          # [mss]             v6.1.0+
import numpy as np  # [numpy]           v1.21.3+
import pyvirtualcam # [pyvirtualcam]    v0.8.0+
import PIL.Image    # [Pillow]          v8.4.0+
import rich.console # [rich]            v10.12.0+

# evn setup
parser = argparse.ArgumentParser()
parser.add_argument("--top", required = True, type = int, help = "where the bounding box starts (from the top of the screen)")
parser.add_argument("--left", required = True, type = int, help ="where the bounding box starts (from the left of the screen)")
parser.add_argument("--width", required = True, type = int, help = "width of the bounding box")
parser.add_argument("--height", required = True, type = int, help = "height of the bounding box")
parser.add_argument("--fps", default = 10, type = int, choices = [1, 10, 30, 60], metavar = "[1, 10, 30, 60]", help = "FPS during capturing and streaming")
parser.add_argument("--preview", help = "render real-time preview", action = "store_true")
args = parser.parse_args()

# bounding box
config = f"[FPS={args.fps}] screen(top={args.top}, left={args.top}, width={args.width}, height={args.height})"
bbox = {"top": args.top, "left": args.left, "width": args.width, "height": args.height}

# init screen capture and vcam
with mss.mss() as sct:
    with pyvirtualcam.Camera(width = args.width, height = args.height, fps = args.fps) as cam:
        with rich.console.Console().status(f"[bold green]streaming to {cam.device} {config}...") as status:
            while True:
                
                # RGB image buffer
                buffer = np.zeros((cam.height, cam.width, 3), np.uint8)

                # grab
                screen = sct.grab(bbox)

                # show preview if enabled
                if args.preview:
                    title="screen2vcam (press \"q\" to stop)"
                    cv2.imshow(title, np.array(screen))
                    cv2.setWindowProperty(title, cv2.WND_PROP_TOPMOST, 1)
                    if (cv2.waitKey(1) & 0xFF) == ord("q"):
                        cv2.destroyAllWindows()
                        break

                # convert and fire to vcam
                buffer[:] = PIL.Image.frombytes("RGB", screen.size, screen.rgb).transpose(PIL.Image.FLIP_LEFT_RIGHT)
                cam.send(buffer)
                cam.sleep_until_next_frame()