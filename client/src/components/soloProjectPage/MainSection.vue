<template>
   <div class="project-container">
      <div class="overflow-hidden">
         <div class="project">
            <div class="image-container">
               <div class="blackout"> </div>
               <div class="gradient"> </div>
               <div class="image">
                  <img v-if="project.image_set.length > 0" :src="`${backendUrl}` + project.image_set[0].image" :alt="project.image_set[0].alt">
                  <img class="no-image" v-else :src="`${frontendUrl}/src/assets/images/no-image.jpg`" alt="There is no images for this project. Try later..">
               </div>
            </div>
            <div class="text-container">

               <router-link v-if="apiEndpoint==='True'" :to="{ name: 'projects' }" class="back-container">
                  <button type="button" class="arrow-back">
                     <i class="el-icon">
                        <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
                           <path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path>
                        </svg>
                     </i>
                  </button>
                  <div class="back-link">
                    {{ text.back_button }}
                  </div>
               </router-link>


              <router-link v-else :to="{ name: 'teamProjects' }" class="back-container">
                  <button type="button" class="arrow-back">
                     <i class="el-icon">
                        <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
                           <path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path>
                        </svg>
                     </i>
                  </button>
                  <div class="back-link">
                     {{ text.back_button }}
                  </div>
               </router-link>

               <h1 v-if="lang_ru" class="title">
                  {{ project.name_ru }}
               </h1>

              <h1 v-else class="title">
                  {{ project.name }}
              </h1>

               <p v-if="lang_ru" class="description">
                  {{project.description_ru}}
               </p>

              <p v-else class="description">
                  {{project.description}}
              </p>

               <div class="additional">
                  <div class="groups">
                     {{project.get_group}}
                  </div>
                  <div class="links">
                     <a v-if="project.git" :href="project.git" class="navbar_social-link w-inline-block" target="_blank">
                        <div class="project-icons">
                           <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                              <path d="M12,0a12.11,12.11,0,0,0-3.8,23.58c.6.12.82-.26.82-.58s0-1.25,0-2.25c-3.34.72-4-1.44-4-1.44a3.11,3.11,0,0,0-1.33-1.76c-1.09-.74.08-.74.08-.74a2.53,2.53,0,0,1,1.85,1.24,2.55,2.55,0,0,0,3.5,1,2.56,2.56,0,0,1,.75-1.62c-2.66-.28-5.47-1.32-5.47-6A4.74,4.74,0,0,1,5.59,8.21,4.36,4.36,0,0,1,5.71,5s1-.32,3.3,1.24a11.29,11.29,0,0,1,3-.4,11.54,11.54,0,0,1,3,.4C17.3,4.69,18.31,5,18.31,5a4.36,4.36,0,0,1,.12,3.2,4.65,4.65,0,0,1,1.24,3.25c0,4.65-2.81,5.67-5.49,6A2.89,2.89,0,0,1,15,19.67c0,1.62,0,2.93,0,3.33s.22.7.82.58A12.11,12.11,0,0,0,12,0Z" fill="currentColor"/>
                           </svg>
                        </div>
                     </a>
                     <a v-if="project.link" :href="project.link" class="navbar_social-link w-inline-block" target="_blank">
                        <div class="project-icons">
                           <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                              <path d="M23.7,11.29,21.22,8.87A13.11,13.11,0,0,0,12,5.15,13.09,13.09,0,0,0,2.78,8.87L.3,11.29a1,1,0,0,0,0,1.43l2.48,2.42A13.12,13.12,0,0,0,12,18.85a13.14,13.14,0,0,0,9.22-3.71l2.48-2.42a1,1,0,0,0,0-1.43ZM12,15.42A3.42,3.42,0,1,1,15.42,12,3.42,3.42,0,0,1,12,15.42ZM2.43,12l1.75-1.7A10.91,10.91,0,0,1,8.87,7.58a5.4,5.4,0,0,0,0,8.83A11,11,0,0,1,4.18,13.7L2.43,12Zm17.39,1.71a11.07,11.07,0,0,1-4.69,2.7,5.39,5.39,0,0,0,0-8.82,11,11,0,0,1,4.69,2.71L21.56,12l-1.74,1.7Z" fill="currentColor"/>
                           </svg>
                        </div>
                     </a>
                  </div>
               </div>
               <div class="button-bottom" v-if="project.image_set.length > 1">
                  <button type="button" class="arrow">
                     <i class="el-icon">
                        <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
                           <path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path>
                        </svg>
                     </i>
                  </button>
               </div>
            </div>
         </div>
      </div>
      <div class="additional-images" v-for="image in project.image_set.slice(1)">
         <a :href="`${this.backendUrl}` + image.image" target="_blank">
         <img :src="`${this.backendUrl}` + image.image" :alt="image.alt">
         </a>
      </div>
      <div class="back-button" v-if="project.image_set.length > 1">

        <router-link v-if="apiEndpoint==='True'" :to="{ name: 'projects' }">
            <button type="button" class="arrow-back">
               <i class="el-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
                     <path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path>
                  </svg>
               </i>
            </button>
            <div class="back-link">
               {{ text.back_button }}
            </div>
         </router-link>

        <router-link  v-else :to="{ name: 'teamProjects' }">
            <button type="button" class="arrow-back">
               <i class="el-icon">
                  <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
                     <path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path>
                  </svg>
               </i>
            </button>
            <div class="back-link">
              {{ text.back_button }}
            </div>
         </router-link>

      </div>
   </div>
</template>

<script>
import axios from "axios";
import store from "../../store";

export default {
  name: "MainSection",
  props: [
    'backendUrl',
    'frontendUrl',
    'apiEndpoint',
    'text'
  ],
  data(){
    return {
      projects: [],
      project: {
        image_set: [],
      },
      lang_ru: false,
    }
  },
  methods: {
    switchLanguage(lang) {
      this.lang_ru = lang === 'ru';
    },

    async get_projects(){
      await axios
        .get(`api/v1/projects/${this.$route.params.id}/`)
        .then(response => {
          this.project = response.data
          // console.log(this.project)
        })
        .catch(error => {
          console.log('Ошибка при загрузке проектов')
          console.log('retrying..')
            setTimeout(() => {
              this.get_projects()
            }, 1000)
        })
    },
  },

  created() {
    this.get_projects()

    store.subscribe((mutation, state) => {
      if (mutation.type === 'language/setLanguage'){
        this.switchLanguage(state.language.language)
      }
    })
  },

  beforeMount() {
    this.switchLanguage(this.$store.state.language.language)
  },
}
</script>

<style scoped>
.project {
     height: 100vh!important;
     position: relative;
}
 .overflow-hidden{
     overflow: hidden;
     position: relative;
}
 .blackout {
     height: 100vh;
     width: 100%;
     position: absolute;
     background-color: rgba(0, 0, 0, 0.3);
     z-index: 99;
}
 .gradient {
     top: 1%;
}
 .back-container{
     display: flex;
     width: max-content;
     margin: 0 0 2rem 2rem;
     color: white;
     padding: 5px 10px;
     background-color: rgba(0, 0, 0, 0.7);
     border-radius: 15px;
}
 .back-container > .back-link{
     margin-right: 15px;
     color: white;
}
 .back-container > .arrow-back{
     color: white;
     background-color: transparent;
}
 .text-container {
     top: 40%;
     height: 50vh;
     display: flex;
     flex-direction: column;
     justify-content: flex-end;
}
 .title {
     padding-bottom: 2rem;
}
 .text-container:hover .title {
     transform: none;
}
 .text-container:hover .additional {
     transform: none;
}
 .navbar_social-link {
     color: white;
}
 .description {
     opacity: 1;
     max-width: 100%;
     padding-bottom: 2rem;
     transform: none;
}
 .additional {
     margin-left: 2rem;
     margin-bottom: 2rem;
}
 .project-icons{
     padding-left: 20px;
}
 .groups {
     padding-bottom: 0.8rem;
}
 .button-bottom{
     height: 50px;
     display: flex;
     justify-content: center;
     align-items: center;
     pointer-events: none;
}
 .arrow {
     border-radius: 50%;
     background-color: rgb(255,255,255, 0.1);
     color: #fff;
     text-align: center;
     font-size: 1rem;
     display: inline-flex;
     justify-content: center;
     align-items: center;
     padding: 10px;
     position: relative;
     animation-name: bounce;
     animation-duration: 1s;
     animation-timing-function: ease-in-out;
     animation-iteration-count: infinite;
     cursor: default;
}
 @keyframes bounce {
     0% {
         top: 0;
    }
     50% {
         top: 50px;
    }
     100% {
         top: 0;
    }
}
 .el-icon {
     transform: rotate(90deg)
}
 .additional-images {
     background-color: rgb(255, 255, 255);
}
 .additional-images img{
     display:block;
     width:100%;
     height:100%;
     object-fit: cover;
     padding: 5vw;
}
 .back-button{
     width: 100%;
     display: flex;
     justify-content: center;
     padding-bottom: 2rem;
     text-align: center;
     background-color: rgb(255, 255, 255);
}
 .back-button > a{
     display: flex;
}
 .arrow-back {
     border-radius: 50%;
     background-color: rgb(255,255,255, 0.1);
     color: #000000;
     text-align: center;
     font-size: 1rem;
     display: inline-flex;
     justify-content: center;
     align-items: center;
     padding: 10px;
     position: relative;
     transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out, transform 0.2s ease-in-out;
}
 .arrow-back > .el-icon{
     transform: rotate(180deg);
}
 .back-button > a:hover .arrow-back{
     color: #ff5e29;
     background-color: rgba(0, 0, 0, 0.1);
     transform: translateX(-10px);
}
 .back-button > a:hover .back-link{
     color: #ff5e29;
}
 .back-link {
     padding: 0.5rem 0rem;
     transition: color 0.2s ease-in-out;
     color: black;
     font-family: Montserrat, 'sans-serif';
     font-style: normal;
     font-weight: 400;
     font-size: 20px;
}
 a:link {
     text-decoration: none;
}
 a:visited {
     text-decoration: none;
}
 a:hover {
     text-decoration: none;
}
 a:active {
     text-decoration: none;
}
</style>