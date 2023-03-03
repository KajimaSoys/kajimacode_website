<template>
<!--  <InDevelop :frontendUrl="frontendUrl"/>-->
  <div class="main-block">
    <h1 class="heading-xlarge">My skills</h1>
    <div class="skills-container">


      <div ref="frontend" @click="expandCard($refs.frontend)" class="card-container" :class="hidden ? 'hidden' : 'visible'">
        <el-card shadow="hover">
          <div class="primary-text" :class="primary ? 'full-opacity' : 'zero-opacity'">
            <h1 class="heading-xxsmall">
                Frontend
              </h1>

              <div class="text-size-medium">
                description
              </div>
          </div>

          <div class="secondary-text" :class="!primary ? 'full-opacity' : 'zero-opacity'">
            <el-collapse v-model="frontendActiveName" accordion>
              <el-collapse-item title="Vue.js" name="1" number="1" @mouseenter="frontendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="HTML" name="2" number="2" @mouseenter="frontendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="CSS" name="3" number="3" @mouseenter="frontendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="JavaScript" name="4" number="4" @mouseenter="frontendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="Jquery" name="5" number="5" @mouseenter="frontendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>

        </el-card>
      </div>

      <div ref="backend" @click="expandCard($refs.backend)" class="card-container" :class="hidden ? 'hidden' : 'visible'">
        <el-card shadow="hover" >
          <div class="primary-text" :class="primary ? 'full-opacity' : 'zero-opacity'">
            <h1 class="heading-xxsmall">
                Backend
              </h1>

              <div class="text-size-medium">
                description
              </div>
          </div>

          <div class="secondary-text" :class="!primary ? 'full-opacity' : 'zero-opacity'">
            <el-collapse v-model="backendActiveName" accordion>
              <el-collapse-item title="Django" name="1" number="1" @mouseenter="backendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="Python" name="2" number="2" @mouseenter="backendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="Nginx/Apache" name="3" number="3" @mouseenter="backendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="Gunicorn" name="4" number="4" @mouseenter="backendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="FastAPI" name="5" number="5" @mouseenter="backendActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>

        </el-card>
      </div>

      <div ref="other" @click="expandCard($refs.other)" class="card-container" :class="hidden ? 'hidden' : 'visible'">
        <el-card shadow="hover" >
          <div class="primary-text" :class="primary ? 'full-opacity' : 'zero-opacity'">
            <h1 class="heading-xxsmall">
              Other
            </h1>

            <div class="text-size-medium">
              description
            </div>
          </div>

          <div class="secondary-text" :class="!primary ? 'full-opacity' : 'zero-opacity'">
            <el-collapse v-model="otherActiveName" accordion>
              <el-collapse-item title="Docker" name="1" number="1" @mouseenter="otherActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="RabbitMQ" name="2" number="2" @mouseenter="otherActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="PostgreSQL" name="3" number="3" @mouseenter="otherActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="Supervisor" name="4" number="4" @mouseenter="otherActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
              <el-collapse-item title="Other SQL-like databases" name="5" number="5" @mouseenter="otherActiveNameChange">
                <div>
                  test text
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>

      </el-card>
      </div>

    </div>

  </div>
</template>

<script>
import InDevelop from "../InDevelop.vue";

export default {
  name: "MainSection",
  components: {
    InDevelop
  },
  props: [
    'backendUrl',
    'frontendUrl'
  ],
  data () {
    return {
      hidden: false,
      primary: true,
      frontendActiveName: '0',
      backendActiveName: '0',
      otherActiveName: '0',
    }
  },
  methods: {
    expandCard(ref){
      if (!this.hidden) {
        ref.style.height = '100%'
        ref.style.visibility = 'visible'
        this.hidden = true
        this.primary = false
      }
      else {
        ref.style.height = ''
        ref.style.visibility = ''
        this.hidden = false
        this.primary = true
      }
    },

    frontendActiveNameChange: function (event){
      if (this.hidden) {
        console.log('Мышь зашла сюда')
        // console.log(event.target.attributes)
        this.frontendActiveName = event.target.getAttribute("number")
      }
    },

    backendActiveNameChange: function (event){
      if (this.hidden) {
        this.backendActiveName = event.target.getAttribute("number")
      }
    },

    otherActiveNameChange: function (event){
      if (this.hidden) {
        this.otherActiveName = event.target.getAttribute("number")
      }
    },
  }
}
</script>

<style scoped>
  .main-block {
    height: 100vh;
    padding-top: 9vh;
    max-width: 80rem;
    margin-left: auto;
    margin-right: auto;
  }

  .skills-container {
    padding: 2rem;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }

  .heading-xlarge {
    margin-top: 3rem;
  }

  .card-container {
    transition: height 0.4s ease-in-out;
}

  .visible {
    height: 30%;
  }

  .hidden {
    height: 0;
    visibility: hidden;
  }

  .primary-text, .secondary-text {
    transition: opacity 0.2s ease-in-out, height 0.5s ease-in-out;
  }

  .full-opacity {
    opacity: 1;
  }

  .zero-opacity {
    opacity: 0;
    height: 0;
    visibility: collapse;
  }

  .el-card.is-hover-shadow {
    height: 100%;
}
</style>