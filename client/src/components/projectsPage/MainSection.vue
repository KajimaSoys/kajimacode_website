<template>
  <div class="project-container">
    <el-carousel :interval="10000" arrow="always">
      <el-carousel-item v-for="project in projects" :key="project.id">
        <div class="image-container">
<!--          FIXME Fix hover-->
          <div class="gradient"> </div>
          <div class="image">
            <img v-if="project.image_set.length !== 0" :src="'http://127.0.0.1:8000' + project.image_set[0].image">
            <img class="no-image" v-else src="src/assets/images/no-image.jpg">
          </div>
        </div>

        <div class="text-container">
          <div class="hover-area"> </div>

          <h1 class="title">
            {{project.name}}
          </h1>

          <p class="description">
            {{project.description}}
          </p>

          <div class="additional">
            <div class="groups">
              {{project.group.name}}
            </div>

            <div class="links">

            </div>
          </div>
        </div>




<!--        <h3 text="2xl" justify="center">keke</h3>-->
      </el-carousel-item>
    </el-carousel>

  <!--    <div class="project" v-for="project in projects">-->
  <!--      <div class="project-img">-->
  <!--        <img v-if="project.image_set.length !== 0" :src="'http://127.0.0.1:8000' + project.image_set[0].image">-->
  <!--        <img v-else src="src/assets/images/no-image.jpg">-->
  <!--      </div>-->

  <!--      {{project.name}}-->

  <!--        <br><br>-->

  <!--      {{project.description}}-->

  <!--      <br><br><br><br>-->

  <!--       {{project.name_ru}}-->

  <!--        <br><br>-->

  <!--      {{project.description_ru}}-->
  <!--    </div>-->
    </div>

</template>

<script>
import axios from "axios";

export default {
  name: "MainSection.vue",
  data(){
    return {
      projects: []
    }
  },
  mounted() {
    this.get_projects()
  },

  methods: {
    async get_projects(){
      await axios
        .get('api/v1/projects/')
        .then(response => {
          this.projects = response.data
          console.log(this.projects)
          // console.log(this.projects.length)
        })
        .catch(error => {
          console.log('Ошибка при загрузке проектов')
        })
    },


  },
}
</script>

<style>
.el-carousel__container {
  height: 100vh!important;
}

.project-container {
  position: absolute;
  top: 0;
  width: 100%;
}

.image-container {
  height: 100vh;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.image-container img{
  max-width: inherit;
  min-width: 100vw;
  height: 100vh;
}


.gradient {
  height: 91vh;
  margin-top: 9vh;
  width: 100%;
  position: absolute;
  --tw-gradient-from: #0f1922;
  --tw-gradient-to: rgb(15 25 34 / 0);
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
  background-image: linear-gradient(to top,var(--tw-gradient-stops));
  top: 20%;
  z-index: 100;
}

.gradient:hover ~ .image{
  transform: scale(1.05);
}

.image {
  transition: transform 0.4s ease-out;
}

.no-image {
  max-width: 100%!important;
  height: auto!important;
}


.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
  text-align: center;
}

.hover-area {
    background-color: transparent;
    width: 100%;
    height: 200%;
    bottom: -25%;
    position: absolute;
    z-index: 105;
}

.text-container {
  position: relative;
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
  top: 65%;
  color: white;
}

.text-container:hover .title {
  transform: translateY(-200%);
}

.text-container:hover .description {
  opacity: 1;
}

.text-container:hover .additional {
  transform: translateY(75%);
}

.title {
  font-family: Montserrat, 'sans-serif';
  font-size: 2rem;
  line-height: 1.1;
  font-style: normal;
  font-weight: bold;
  margin: 0 2rem;
}

.title, .additional {
  transition: all 0.3s ease-in-out;
}

.description {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  margin: 0 2rem;
  opacity: 0;
  transition: all 0.3s ease-in-out;
  transform: translateY(-50%);
  max-width: 60%;
  /*margin-bottom: -50px;*/
}

.additional {
  border-bottom: white solid 1px;
  margin: 0 2rem;
}

.groups {
  padding-bottom: 0.8rem;
}

</style>