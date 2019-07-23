import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Searchbox from '@/components/Searchbox'
import Insert from '@/components/Insert'
import Survey from '@/components/Survey'
import NewSurvey from '@/components/NewSurvey'
import NewSet from '@/components/NewSet'
import Login from '@/components/Login'
import store from '@/store'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/surveys/:id',
      name: 'Survey',
      component: Survey
    },
    { path: '/search',
      component: Searchbox
    },
    { path: '/insert',
      component: Insert
    },
    {
      path: '/surveys',
      name: 'NewSurvey',
      component: NewSurvey
    },
    {
      path: '/set',
      component: NewSet,
      beforeEnter (to, from, next) {
        if (!store.getters.isAuthenticated) {
          next({name: 'Login', query: {redirect: '/set'}})
        } else {
          next()
        }
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
