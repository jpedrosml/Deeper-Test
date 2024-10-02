import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000';

const userService = {
  async getUsers() {
    const response = await axios.get(`${baseURL}/api/users`);
    return response.data;
  },

  async getUser(username) {
    const response = await axios.get(`${baseURL}/api/users/${username}`);
    return response.data;
  },

  async createUser(user) {
    const response = await axios.post(`${baseURL}/api/users`, user);
    return response.data;
  },

  async updateUser(username, user) {
    const response = await axios.put(`${baseURL}/api/users/${username}`, user);
    return response.data;
  },

  async deleteUser(username) {
    const response = await axios.delete(`${baseURL}/api/users/${username}`);
    return response.data;
  },
};

export default userService;