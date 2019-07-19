import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import Searchbox from './components/Searchbox'
import Insert from './components/Insert'
import router from './router'

Vue.use(VueRouter)

// const routes = [
// { path: '/', component: Searchbox },
// { path: '/insert', component: Insert }
// ]

// const router = new VueRouter({
//   routes,
//   mode: 'history'
// })

new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router
}).$mount('#app')
