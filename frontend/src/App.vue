    // src/App.vue
	
    <template>
      <div id="app">
      
      <router-link v-bind:to="'/'">HOME</router-link>   |  
      <router-link v-bind:to="'/insert'">INSERT</router-link>   |  
        <router-link v-bind:to="'/search'">SEARCH</router-link>
      <router-view></router-view>
      
      </div>
    </template>
    
    <script>
    export default {
      name: 'app',
    }
    </script>

    <style lang="scss">
    @import '~bulma/bulma'
    </style>
