import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/projects',
      name: 'Projects',
      component: () => import('../pages/ProjectsPage.vue')
    },
    {
      path: '/pr',
      name: 'PullRequests',
      component: () => import('../pages/PullRequestsPage.vue')
    },
    {
      path: '/issues',
      name: 'Issues',
      component: () => import('../pages/IssuesPage.vue')
    }
  ]
})

export default router
