import strip
import pathlib

sample = pathlib.Path('../test/fixtures/strip-all.js').read_text()
banner = pathlib.Path('../test/fixtures/banner.js').read_text()

# print(strip.first(sample))
# print(strip.block(sample))
# print(strip.line(sample))
print(strip.strip(sample))
