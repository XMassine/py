import io
from PIL import Image
from fs import FS
from mem import Mem


def display_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image.show()


def main():
    fs = FS("images")
    mem = Mem(capacity=3)

    source_file = "test1.jpg"  # put this inside /images

    print("=== FILE SYSTEM TEST ===")

    data, read_time = fs.read(source_file)
    print(f"Read time (FS): {read_time:.6f} sec")

    write_time = fs.create("copy_fs.jpg", data)
    print(f"Write time (FS): {write_time:.6f} sec")

    data2, _ = fs.read("copy_fs.jpg")
    display_image(data2)

    print("\n=== MEMCACHED TEST ===")

    write_time_mem = mem.create("img1", data)
    print(f"Write time (RAM): {write_time_mem:.6f} sec")

    data_mem, read_time_mem = mem.read("img1")
    print(f"Read time (RAM): {read_time_mem:.6f} sec")

    if data_mem:
        display_image(data_mem)


if __name__ == "__main__":
    main()
