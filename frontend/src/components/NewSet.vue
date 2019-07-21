<template>
  <div>
    <label for="exercise">exercise</label>
    <input type="text" id="exercise" v-model="set.exercise"><br>

    <label for="weight">weight</label>
    <input type="number" id="weight" v-model="set.weight"><br>

    <label for="bar">bar</label>
    <input type="number" id="bar"><br>

    <label for="collars">collars</label>
    <input type="number" id="collars"><br>

    <label for="bodyweight">bodyweight</label>
    <input type="number" id="bodyweight" v-model="set.bodyweight"><br>

    <label for="reps">reps</label>
    <input type="number" id="reps" v-model="set.reps"><br>

    <label for="rpe">rpe</label>
    <input type="number" id="rpe" v-model="set.rpe"><br>

    <label for="notes">notes</label>
    <input type="text" id="notes" v-model="set.notes"><br>

    <div class="control">
      <a class="button is-large is-primary" @click="submitSet">Submit</a>
      <a class="button is-large is-primary" @click="loadSet">Load</a>
    </div>

  </div>
</template>


<script>
  export default {
    data() {
      return {
        set: {
          exercise: '',
          weight: 0,
          bodyweight: 0,
          reps: 0,
          rpe: 0,
          notes: ''
        }
      }
    },
    methods: {
      submitSet() {
        this.$store.dispatch('submitSet', this.set)
          .then(() => this.$router.push('/'))
      },
      loadSet() {
        this.$store.dispatch('loadSet')
          .then(() => this.$router.push('/'))
      }
    }
  }
</script>

<style>
  .question {
    margin: 10px 20px 25px 10px;
  }

  .delete-question {
    cursor: pointer;
    padding: 10px;
  }

  .delete-question:hover {
    background-color: lightgray;
    border-radius: 50%;
  }
</style>
