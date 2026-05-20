const { createRequire } = require("module");
const path = require("path");

const requireFromRuntime = createRequire(
  "/Users/vitor/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/"
);
const sharp = requireFromRuntime("sharp");

const input =
  "/private/var/folders/qt/yl4tlc1s3xl_11lvn5t7wkrc0000gn/T/com.apple.Photos.NSItemProvider/uuid=DA1EF513-9371-4EA2-98E9-331279E4686D&code=001&library=1&type=1&mode=2&loc=true&cap=true.jpeg/IMG_1474.jpeg";

const output = path.resolve(
  __dirname,
  "../assets/gallery/paint-correction/paint-correction-cover.jpg"
);

async function buildCover() {
  const width = 1200;
  const height = 810;

  const base = await sharp(input)
    .rotate()
    .extract({ left: 0, top: 840, width: 3024, height: 2043 })
    .resize(width, height, { fit: "cover", position: "centre" })
    .modulate({ brightness: 0.92, saturation: 0.88 })
    .linear(1.08, -10)
    .sharpen({ sigma: 0.8 })
    .toBuffer();

  const vignette = Buffer.from(`
    <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="top" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#02050a" stop-opacity="0.34"/>
          <stop offset="0.42" stop-color="#02050a" stop-opacity="0.04"/>
          <stop offset="1" stop-color="#02050a" stop-opacity="0.16"/>
        </linearGradient>
        <radialGradient id="edge" cx="54%" cy="47%" r="74%">
          <stop offset="0.48" stop-color="#000000" stop-opacity="0"/>
          <stop offset="1" stop-color="#000000" stop-opacity="0.42"/>
        </radialGradient>
      </defs>
      <rect width="100%" height="100%" fill="url(#top)"/>
      <rect width="100%" height="100%" fill="url(#edge)"/>
    </svg>
  `);

  await sharp(base)
    .composite([{ input: vignette, blend: "over" }])
    .jpeg({ quality: 88, mozjpeg: true })
    .toFile(output);
}

buildCover().catch((error) => {
  console.error(error);
  process.exit(1);
});
