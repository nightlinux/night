import tarfile
import zstandard as zstd

def extract_night(file_path, output_dir):
    with open(file_path, 'rb') as compressed_file:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(compressed_file) as decompressed:
            with tarfile.open(fileobj=decompressed, mode='r:') as tar:
                tar.extractall(path=output_dir)

extract_night('/home/shin/nightlinux/night/test/cool.tar.zst', '/home/shin/nightlinux/night/test')
