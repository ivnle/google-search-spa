<template>
  <div>
    <label for="exercise">exercise</label>
    <input type="text" id="exercise"><br>

    <label for="weight">weight</label>
    <input type="number" id="weight"><br>

    <label for="bar">bar</label>
    <input type="number" id="bar"><br>

    <label for="collars">collars</label>
    <input type="number" id="collars"><br>

    <label for="bodyweight">bodyweight</label>
    <input type="number" id="bodyweight"><br>

    <label for="reps">reps</label>
    <input type="number" id="reps"><br>

    <label for="rpe">rpe</label>
    <input type="number" id="rpe"><br>

    <label for="notes">notes</label>
    <input type="text" id="notes"><br>


  </div>
</template>


<script>
import NewQuestion from '@/components/NewQuestion'

export default {
  components: { NewQuestion },
  data () {
    return {
      step: 'name',
      name: '',
      questions: []
    }
  },
  methods: {
    appendQuestion (newQuestion) {
      this.questions.push(newQuestion)
    },
    removeQuestion (question) {
      const idx = this.questions.findIndex(q => q.question === question.question)
      this.questions.splice(idx, 1)
    },
    submitSurvey () {
      this.$store.dispatch('submitNewSurvey', {
        name: this.name,
        questions: this.questions
      }).then(() => this.$router.push('/'))
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
