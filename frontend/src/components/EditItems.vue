<template>
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">{{ msg }}</div>
        <div class="card-body">
          <div class="form-group row">
            <label for="item_title" class="col-md-4 col-form-label text-md-right">Item Title</label>
            <div class="col-md-6">
              <input
                type="text"
                id="item_title"
                class="form-control"
                name="item_title"
                v-model="title"
                required
                autofocus
              />
            </div>
          </div>

          <div class="form-group row">
            <label for="item_description" class="col-md-4 col-form-label text-md-right">Item Description</label>
            <div class="col-md-6">
              <textarea id="item_description" name="item_description" class="form-control" rows="5" v-model="description"></textarea>
            </div>
          </div>

          <div class="form-group row">
            <label for="item_ranking" class="col-md-4 col-form-label text-md-right">Item Ranking</label>
            <div class="col-md-6">
              <input
                type="number"
                id="item_ranking"
                class="form-control"
                name="item_ranking"
                v-model="ranking"
                required
                autofocus
              />
            </div>
          </div>

          <div class="form-group row">
            <label for="item_category" class="col-md-4 col-form-label text-md-right">Item Category</label>
            <div class="col-md-6">
              <select v-model="category" id="item_category" class="form-control" name="item_category" required autofocus placeholder="Select Desired Category">
                <option v-for="option in this.categories" v-bind:key="option.id" :value="option.id">
                  {{ option.name }}
                </option>
              </select>
            </div>
          </div>

          <div class="form-group row">
            <label for="item_metadata" class="col-md-4 col-form-label text-md-right">Item Metadata</label>
            <div class="col-md-6">
              <select v-model="metadata" id="item_metadata" class="form-control" name="item_metadata" required autofocus placeholder="Select Desired Metadata">
                <option v-for="option in this.allmetadata" v-bind:key="option.id" :value="option.id">
                  {{ option.key + ' : ' + option.value }}
                </option>
              </select>
            </div>
          </div>
          <div class="col-md-6 offset-md-4">
            <button type="button" class="btn btn-primary" @click="updateItem">Save</button>
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
  name: 'EditItems',
  data: () => ({
    title: '',
    ranking: '',
    metadata: '',
    category: '',
    description: '',
    item: [],
    items: [],
    message: '',
    categories: [],
    allmetadata: [],
    msg: 'Editing'
  }),
  mounted () {
    this.getAllData()
  },
  methods: {
    getAllData () {
      apiService.getData('items').then(data => {
        this.items = data.items
      })

      apiService.getData('metadata').then((data) => {
        this.allmetadata = data.metadata
      })

      apiService.getData('categories').then((data) => {
        this.categories = data.categories
      })

      apiService.getSpecificData('items', this.$route.params.id).then(data => {
        this.item = data.item
        this.title = data.item.title
        this.ranking = data.item.ranking
        this.category = data.item.category
        this.metadata = data.item.metadata
        this.description = data.item.description
        this.msg = `Editing Items '${this.title}'`
      })
    },
    updateItem () {
      this.item.title = this.title
      this.item.ranking = this.ranking
      this.item.category = this.category
      this.item.metadata = this.metadata
      this.item.description = this.description

      apiService.updateData('items', this.item).then(data => {
        if (data.status === 201 && data.data.status === 'success') {
          this.message = `Succesfully created favourite item '${this.description}'`
          this.title = ''
          this.ranking = ''
          this.metadata = ''
          this.category = ''
          this.description = ''
        } else {
          this.message = data.data
        }
      })
    }
  }
}
</script>
