class Codec:
    def __init__(self):
        self.arr=[]

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.arr.append(longUrl)
        return str(len(self.arr)-1)
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.arr[int(shortUrl)]
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))