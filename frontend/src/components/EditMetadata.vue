<template>
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">{{ msg }}</div>
        <div class="card-body">
          <div class="form-group row">
            <label for="metadata_key" class="col-md-4 col-form-label text-md-right">Metadata Key</label>
            <div class="col-md-6">
              <input
                type="text"
                id="metadata_key"
                class="form-control"
                name="metadata_key"
                v-model="key"
                required
                autofocus
              />
            </div>
          </div>

          <div class="form-group row">
            <label for="metadata_value" class="col-md-4 col-form-label text-md-right">Metadata Value</label>
            <div class="col-md-6">
              <input
                type="text"
                id="metadata_value"
                class="form-control"
                name="metadata_value"
                v-model="value"
                required
                autofocus
              />
            </div>
          </div>

          <div class="col-md-6 offset-md-4">
            <button type="button" class="btn btn-primary" @click="updateMetadata">Save</button>
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
  name: 'EditMetadata',
  data: () => ({
    msg: '',
    key: '',
    value: '',
    message: '',
    metadata: [],
    allmetadata: []
  }),
  mounted () {
    this.getMetadata()
  },
  methods: {
    getMetadata () {
      apiService.getSpecificData('metadata', this.$route.params.id).then(data => {
        this.key = data.metadata.key
        this.value = data.metadata.value
        this.metadata = data.metadata
        this.msg = `Editing Key '${this.key}'`
      })

      apiService.getData('metadata').then(data => {
        this.allmetadata = data.metadata
      })
    },
    updateMetadata () {
      this.metadata.key = this.key
      this.metadata.value = this.value
      apiService.updateData('metadata', this.metadata).then(data => {
        if (data.status === 200 && data.data.status === 'success') {
          this.message = `Succesfully updated key/value '${this.key}/${this.value}'`
          this.key = ''
          this.value = ''
        } else {
          this.message = data.data.errors
        }
      })
    }
  }
}
</script>
