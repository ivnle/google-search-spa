import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Searchbox from '@/components/Searchbox'
import Insert from '@/components/Insert'
import Survey from '@/components/Survey'

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
      component: Insert }
  ]
})
