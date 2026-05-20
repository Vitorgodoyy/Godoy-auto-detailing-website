const { createRequire } = require("module");
const path = require("path");

const requireFromRuntime = createRequire(
  "/Users/vitor/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/"
);
const sharp = requireFromRuntime("sharp");

const covers = [
  {
    input:
      "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=F75A6035-70E8-4A4B-A232-D70DD6C781A6&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_1868.jpeg",
    output: "../assets/gallery/paint-correction/porsche-paint-correction-cover.jpg",
    position: "attention",
  },
  {
    input:
      "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=66BE7DCC-44D5-42A1-A7D2-95CB00EA2657&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_1854.jpeg",
    output: "../assets/gallery/paint-correction/porsche-paint-correction-close-cover.jpg",
    position: "attention",
  },
];

async function makeCover({ input, output, position }) {
  const width = 1200;
  const height = 810;
  const outPath = path.resolve(__dirname, output);

  const base = await sharp(input)
    .rotate()
    .resize(width, height, { fit: "cover", position })
    .modulate({ brightness: 0.94, saturation: 0.9 })
    .linear(1.12, -12)
    .sharpen({ sigma: 0.75 })
    .toBuffer();

  const overlay = Buffer.from(`
    <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="shade" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#02050a" stop-opacity="0.30"/>
          <stop offset="0.48" stop-color="#02050a" stop-opacity="0"/>
          <stop offset="1" stop-color="#02050a" stop-opacity="0.26"/>
        </linearGradient>
        <radialGradient id="edge" cx="54%" cy="48%" r="74%">
          <stop offset="0.54" stop-color="#000000" stop-opacity="0"/>
          <stop offset="1" stop-color="#000000" stop-opacity="0.34"/>
        </radialGradient>
      </defs>
      <rect width="100%" height="100%" fill="url(#shade)"/>
      <rect width="100%" height="100%" fill="url(#edge)"/>
    </svg>
  `);

  await sharp(base)
    .composite([{ input: overlay, blend: "over" }])
    .jpeg({ quality: 88, mozjpeg: true })
    .toFile(outPath);
}

Promise.all(covers.map(makeCover)).catch((error) => {
  console.error(error);
  process.exit(1);
});
