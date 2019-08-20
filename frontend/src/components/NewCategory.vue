<template>
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">{{ msg }}</div>
        <div class="card-body">
          <div class="form-group row">
            <label for="category_name" class="col-md-4 col-form-label text-md-right">Category Name</label>
            <div class="col-md-6">
              <input
                type="text"
                id="category_name"
                class="form-control"
                name="category_name"
                v-model="name"
                required
                autofocus
              />
            </div>
          </div>

          <div class="col-md-6 offset-md-4">
            <button type="button" class="btn btn-primary" @click="newCategory">Save</button>
          </div>

          <div id="message">
            {{message}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { APIService } from '../APIService'
const apiService = new APIService()

export default {
  name: 'NewCategory',
  data: () => ({
    name: '',
    message: '',
    categories: [],
    msg: 'Create New Category'
  }),
  mounted () {
    this.getCategories()
  },
  methods: {
    getCategories () {
      apiService.getData('categories').then(data => {
        this.categories = data.categories
      })
    },
    newCategory () {
      // Check to make sure category does not exist
      let IsValid = this.categories.filter((item) => {
        return item.name === this.name
      })

      if (IsValid.length >= 1) {
        this.message = `Category '${this.name}' already exists.`
        return
      }

      apiService.createData('categories', { name: this.name }).then(data => {
        if (data.status === 201 && data.data.status === 'success') {
          this.message = `Succesfully created category '${this.name}'`
          this.name = ''
        } else {
          this.message = data.data.errors
        }
      })
    }
  }
}
</script>
