<template>
  <div class="loading" @click="stopAnimation" ref="loading">
    <div class="render" ref="render">
      <canvas class="ascii-canvas" ref="canvas" aria-hidden="true"></canvas>
    </div>

    <div class="stop" ref="stop">
      {{ this.$store.state.language.language === 'ru' ? 'Пропустить..' : 'Click to continue..' }}
    </div>

    <div class="backdown" ref="backdown">
      <div class="left" ref="left"></div>
      <div class="right" ref="right"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

// Geometry of a single ascii cell in logical units, the canvas is scaled to fit the screen
const FONT_SIZE = 10.5;
const CHAR_WIDTH = 6.3;
const LINE_HEIGHT = 13;
const FONT = `${FONT_SIZE}px ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', 'DejaVu Sans Mono', monospace`;
const FRAME_DELAY = 30;
const MAX_RETRIES = 3;

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

export default {
  name: "AsciiRender",
  data() {
    return {
      num_files: 20,
      ascii_active: true,
    }
  },
  methods: {
    async get_ascii(index) {
      let retries = 0;
      while (this.ascii_active && index <= this.num_files) {
        try {
          const response = await axios.get(`api/v1/get_ascii_part_${index}`);
          if (!Array.isArray(response.data.res)) {
            throw new Error(`ascii part ${index} is unavailable`);
          }
          this.ascii_array[response.data.key] = response.data.res

          if (index === 1) {
            this.build_text_attrs()
          }
          index++;
          retries = 0;
        } catch (error) {
          console.log(error);
          if (++retries > MAX_RETRIES) {
            this.num_files = index - 1;
            if (index === 1) {
              this.stopAnimation()
            }
            return;
          }
          await sleep(1000 * retries); // retry downloading the same file if an error occurs
        }
      }
    },

    async build_text_attrs() {
      const firstFrame = this.ascii_array[1][0];
      this.cols = Math.max(...firstFrame.map(row => row.length));
      // every frame ends with an empty separator row
      this.rows = firstFrame[firstFrame.length - 1].length ? firstFrame.length : firstFrame.length - 1;
      this.fitCanvas();

      for (let i = 1; i <= this.num_files && this.ascii_active; i++) {
        while (!this.ascii_array[i] && i <= this.num_files && this.ascii_active) {
          await sleep(100);
        }
        const frames = this.ascii_array[i] || [];
        for (const frame of frames) {
          if (!this.ascii_active) {
            return;
          }
          this.drawFrame(frame);
          await sleep(FRAME_DELAY);
        }
      }
      this.stopAnimation()
    },

    fitCanvas() {
      const canvas = this.$refs.canvas;
      const render = this.$refs.render;
      if (!canvas || !render || !this.cols) {
        return;
      }
      const style = getComputedStyle(render);
      const availWidth = render.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
      const availHeight = render.clientHeight - parseFloat(style.paddingTop) - parseFloat(style.paddingBottom);
      const width = this.cols * CHAR_WIDTH;
      const height = this.rows * LINE_HEIGHT;
      const scale = Math.max(Math.min(availWidth / width, availHeight / height), 0);
      const dpr = window.devicePixelRatio || 1;

      canvas.style.width = `${Math.floor(width * scale)}px`;
      canvas.style.height = `${Math.floor(height * scale)}px`;
      canvas.width = Math.max(Math.round(width * scale * dpr), 1);
      canvas.height = Math.max(Math.round(height * scale * dpr), 1);

      const ctx = canvas.getContext('2d');
      ctx.font = FONT;
      // glyph width differs between systems fonts, stretch glyphs to the exact cell grid
      this.glyphScale = CHAR_WIDTH / (ctx.measureText('@').width || CHAR_WIDTH);
      this.ctx = ctx;
      this.transform = [canvas.width / width * this.glyphScale, canvas.height / height];

      if (this.lastFrame) {
        this.drawFrame(this.lastFrame);
      }
    },

    drawFrame(frame) {
      const ctx = this.ctx;
      if (!ctx) {
        return;
      }
      this.lastFrame = frame;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
      ctx.setTransform(this.transform[0], 0, 0, this.transform[1], 0, 0);
      ctx.font = FONT;
      ctx.textBaseline = 'top';
      ctx.fillStyle = 'white';
      const cellWidth = CHAR_WIDTH / this.glyphScale;
      for (let j = 0; j < this.rows && j < frame.length; j++) {
        // each run of symbols is anchored to its own column, so spacing never drifts
        for (const run of frame[j].matchAll(/\S+/g)) {
          ctx.fillText(run[0], run.index * cellWidth, j * LINE_HEIGHT);
        }
      }
    },

    stopAnimation() {
      if (!this.ascii_active) {
        return;
      }
      this.ascii_active = false
      // console.log('stop animation')

      this.$refs.render.style.opacity = '0'
      this.$refs.stop.style.opacity = '0'

      this.timers.push(setTimeout(() => {
        this.$refs.render.style.display = 'none'
        this.$refs.stop.style.display = 'none'
        this.$refs.loading.style.height = '0'
        this.$refs.left.style.transform = 'translateX(-100%)'
        this.$refs.right.style.transform = 'translateX(100%)'
      }, 300))

      this.timers.push(setTimeout(() => {
        this.$refs.backdown.style.display = 'none'
        document.body.style.overflow = 'auto'
      }, 1000))
    }
  },
  created() {
    // frames are kept out of reactive data, they are only drawn on the canvas
    this.ascii_array = {};
    this.timers = [];
    document.body.style.overflow = 'hidden'
    window.scrollTo({top: 0, behavior: 'auto'});
    this.get_ascii(1)
  },
  mounted() {
    this.resizeObserver = new ResizeObserver(() => this.fitCanvas());
    this.resizeObserver.observe(this.$refs.render);
  },
  beforeUnmount() {
    this.ascii_active = false
    this.resizeObserver.disconnect();
    this.timers.forEach(clearTimeout);
    document.body.style.overflow = 'auto'
  },
}
</script>

<style scoped>

.loading {
  background-color: #1d2939;
  position: relative;
  z-index: 1001;
  cursor: pointer;
  height: 100vh;
  height: 100dvh;
}

.render {
  box-sizing: border-box;
  width: 100%;
  max-width: 1200px;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3rem 3rem 7rem;
  transition: opacity 0.3s ease-in-out;
}

.ascii-canvas {
  display: block;
}

.stop {
  color: white;
  text-align: center;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  letter-spacing: normal;
  transition: opacity 0.3s ease-in-out, color 0.2s ease-in-out;
  position: fixed;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  z-index: 1;
  bottom: 60px;
}

.stop:hover {
  color: #ff5f29;
}

.backdown {
  display: flex;
  position: absolute;
  width: 100%;
}

.left {
  width: 50%;
  background-color: #1d2939;
  height: max(1500px, 100vh);
  transition: transform 0.5s ease-in-out;
}

.right {
  width: 50%;
  background-color: #1d2939;
  height: max(1500px, 100vh);
  transition: transform 0.5s ease-in-out;
}

@media screen and (max-width: 767px) {
  .render {
    padding: 1rem 1rem 6rem;
  }
}

@media screen and (max-height: 500px) {
  .render {
    padding: 1rem 1rem 4rem;
  }

  .stop {
    bottom: 1rem;
  }
}
</style>