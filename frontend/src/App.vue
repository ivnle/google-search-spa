    // src/App.vue
	
    <template>
      <div id="app">
      
      <router-link v-bind:to="'/'">      HOME</router-link  >   |  
      <router-link v-bind:to="'/insert'">INSERT</router-link>   |  
      <router-link v-bind:to="'/search'">SEARCH</router-link>

      <my-header></my-header>

      <router-view></router-view>
      
      </div>
    </template>
    
<script>
import MyHeader from '@/components/Header'
export default {
  name: 'App',
  components: { MyHeader }
}
</script>

<style lang="scss">
@import '~bulma/bulma'
</style>
