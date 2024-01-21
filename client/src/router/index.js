import {createRouter, createWebHistory} from 'vue-router'

// Core Views
import MainView from '../views/MainView.vue'
import ProjectsView from "../views/ProjectsView.vue";
import SoloProjectView from "../views/SoloProjectView.vue";
import SkillsView from "../views/SkillsView.vue";
import AboutView from "../views/AboutView.vue";
import CookieView from "../views/CookieView.vue";
import TermsView from "../views/TermsView.vue";
import PrivacyView from "../views/PrivacyView.vue";

// Secondary Views
// import TeamProjectsView from "../views/minorViews/TeamProjectsView.vue";
import AsciiView from "../views/minorViews/AsciiView.vue";
import MainViewBackup from "../views/minorViews/MainViewBackup.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'main',
            component: MainView
        },
        {
            path: '/projects',
            name: 'projects',
            component: ProjectsView
        },
        {
            path: '/projects/team',
            name: 'teamProjects',
            component: ProjectsView
        },
        {
            path: '/projects/:id',
            name: 'project',
            component: SoloProjectView
        },
        {
            path: '/projects/team/:id',
            name: 'teamProject',
            component: SoloProjectView
        },
        {
            path: '/skills',
            name: 'skills',
            component: SkillsView
        },
        {
            path: '/about',
            name: 'about',
            component: AboutView
        },
        {
            path: '/cookies',
            name: 'cookies',
            component: CookieView
        },
        {
            path: '/terms',
            name: 'terms',
            component: TermsView
        },
        {
            path: '/privacy',
            name: 'privacy',
            component: PrivacyView
        },
        {
            path: '/ascii',
            name: 'ascii',
            component: AsciiView,
        },
        {
            path: '/backup',
            name: 'backup',
            component: MainViewBackup
        }
    ],
    // scrollBehavior(to, from, savedPosition) {
    // if (to.hash) {
    // } else if (savedPosition) {
    //   return new Promise(resolve => {
    //     setTimeout(()=>{
    //       savedPosition.behavior = "smooth"
    //       resolve(savedPosition);
    //     }, 1000)
    //   })
    //   // return savedPosition;
    // } else {
    //   return { x: 0, y: 0 };
    // }
// },


})
export default router
