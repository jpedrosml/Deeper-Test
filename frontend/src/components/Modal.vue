<script>
    export default {
        props: {
            show: Boolean,
            user: Object,
            isEdit: Boolean,
        },

        data() {
            return {
                form: {
                    username: '',
                    roles: [],
                    preferences: {
                        timezone: ' ',
                    },

                    active: true,
                },
                rolesInput: '',
            };
        },

        watch: {
            user: {
                handler(newUser) {
                    if (newUser) {
                        this.form = { ...newUser };
                        this.rolesInput = newUser.roles.join(', ');
                    }
                },
                immediate: true,
            },
        },

        methods: {
            submitForm() {
                const formData = { ...this.form };
                formData.roles = this.rolesInput.split(',').map(role => role.trim());
                this.$emit('submit', formData);
            },

            closeModal() {
                this.$emit('close');
            },
        },
    };
</script>

<template>
    <div v-if="show" class="modal-backdrop">
      <div class="modal">
        <h2>{{ isEdit ? 'Edit User' : 'Create User' }}</h2>
        <form @submit.prevent="submitForm">
          <div>
            <label for="username">Username:</label>
            <input id="username" v-model= "form.username" required :disabled="isEdit">
          </div>

          <div>
            <label for="roles">Roles (comma-separated):</label>
            <input id="roles" v-model="rolesInput">
          </div>

          <div>
            <label for="timezone">Timezone:</label>
            <input id="timezone" v-model="form.preferences.timezone" required>
          </div>

          <div>
            <label for="active">Is Active:</label>
            <input id="active" type="checkbox" v-model="form.active">
          </div>

          <div>
            <button type="submit">{{ isEdit ? 'Update' : 'Create' }}</button>
            <button type="button" @click="closeModal">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
 
  
<style scoped>
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        width: 300px;
    }
</style>