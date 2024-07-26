import axios from "axios";
import { user } from "./state/user";
import { currentView } from "./state";

export default class API {
  static init = async () => {
    axios.defaults.baseURL = "http://127.0.0.1:5000/";
    axios.defaults.withCredentials = true;
    await API.user.isLoggedIn();
  };

  static user = {
    isLoggedIn: async () => {
      axios.get("/user/isLoggedIn").then((response) => {
        console.log(response.data);
        if (response.data.success) {
          user.set(response.data.user);
          currentView.set("dashboard");
        }
      });
    },
    logIn: async (email, password) => {
      axios.post("/user/logIn", { email, password }).then((response) => {
        if (response.data.success) {
          currentView.set("dashboard");
          user.set(response.data.user);
        } else {
          alert("Log in failed: " + response.data.message);
        }
      });
    },
    register: async (email, firstName, lastName, password) => {
      axios
        .post("/user/register", {
          email,
          firstName,
          lastName,
          password,
        })
        .then((response) => {
          console.log(response.data);
          if (response.data.success) {
            alert("Registration successful!");
            currentView.set("logIn");
          } else {
            alert("Registration failed: E-mail address already in use");
          }
        });
    },
    logOut: async () => {
      await axios.delete("/user/logOut");
      window.location.href = "/";
    },
    search: async (lastName) => {
      const response = await axios.get("/user/search?lastName=" + lastName);
      return response.data.users;
    },
  };
  static shift = {
    create: (workerId, startTime, endTime, notes) => {
      axios
        .post("/shift/create", { workerId, startTime, endTime, notes })
        .then((response) => {
          console.log(response);
          if (response.data.success) {
            alert("Shift successfully scheduled!");
            currentView.set("dashboard");
          } else {
            alert("Shift could not be created.");
          }
        });
    },
    readByUser: (id, callback) => {
      axios.get("/shift/readByUser?userId=" + id).then((response) => {
        console.log(response.data);
        if (response.data.success) {
          callback(response.data.shifts);
        }
      });
    },
  };
  static clock = {
    create: async (isWorking) => {
      const response = await axios.post("/clock/create");
      if (!response.data.success) {
        alert(isWorking?"Clock Out failed!": "Clock in failed!")
      } else {
        alert("clock " + (isWorking? "out" : "in") + " successful!")
      }
    },
    checkWorking: async () => {
      const response = await axios.get("/clock/checkWorking");
      return response.data.success;
    }
  };
}
