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
      <a :class="submitState" @click="submitSet">
        <span class="icon is-small">
        <i :class="submitIcon"></i>
        </span>
        <span>{{ submitText }}</span>
      </a>
    </div>

  </div>
</template>


<script>

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

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
        },
        submitState: "button is primary is-normal",
        submitText: "save",
        submitIcon: "fas fa-save",
      }
    },
    methods: {
      submitSet() {
        this.submitState = "button is-loading";
        this.$store.dispatch('submitSet', this.set)
          .then(async () => {
            this.submitState = "button is-success";
            this.submitText = "saved";
            this.submitIcon = "fas fa-check";

            await sleep(1000);
            this.submitState = "button is primary is-normal";
            this.submitText = "save";
            this.submitIcon = "fas fa-save";

          })
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
