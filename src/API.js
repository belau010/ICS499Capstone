import axios from "axios";
import { user } from "./state/user";
import { currentView } from "./state";
import ChangePassword from "./templates/ChangePassword.svelte";

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
          if (response.data.user.forcePasswordChange) {
            currentView.set("changePassword");
          } else {
            currentView.set("dashboard");
          }
        }
      });
    },
    logIn: async (email, password) => {
      axios.post("/user/logIn", { email, password }).then((response) => {
        if (response.data.success) {
          if (response.data.user.forcePasswordChange) {
            currentView.set("changePassword");
          } else {
            currentView.set("dashboard");
          }
          user.set(response.data.user);
        } else {
          alert("Log in failed: " + response.data.message);
        }
      });
    },
    ChangePassword: async (newPassword) => {
      axios
        .post("/user/changePassword", {
          newPassword,
        })
        .then((response) => {
          if (response.data.success) {
            alert("Password change successful!");
            currentView.set("dashboard");
          } else {
            alert("Password change failed: " + response.data.message);
          }
        });
    },
    register: async (
      email,
      firstName,
      lastName,
      password,
      payRate,
      position,
      forcePasswordChange
    ) => {
      axios
        .post("/user/register", {
          email,
          firstName,
          lastName,
          password,
          payRate,
          position,
          forcePasswordChange,
        })
        .then((response) => {
          console.log(response.data);
          if (response.data.success) {
            alert("Registration successful!");
          } else {
            alert("Registration failed: " + response.data.message);
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
    update: async (
      id,
      firstName,
      lastName,
      payRate,
      noShowDays,
      callOutDays,
      position,
      forcePasswordChange
    ) => {
      const response = await axios.post("/user/update", {
        id,
        firstName,
        lastName,
        payRate,
        noShowDays,
        callOutDays,
        position,
        forcePasswordChange,
      });
      if (response.data.success) {
        alert("User update successful!");
      } else {
        alert("User update failed: " + response.data.message);
      }
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
    readByDate: async (date) => {
      const response = await axios.get("/shift/readByDate?date=" + date);
      console.log(response.data);
      if (response.data.success) {
        return response.data.shifts;
      }
      return [];
    },
    update: async (id, startTime, endTime, notes) => {
      const response = await axios.post("/shift/update", {id, startTime, endTime, notes});
      if (response.data.success) {
        alert("Shift successfully updated!");
      } else {
        alert("Shift update failed: " + response.data.message);
      }
    }
  };
  static clock = {
    create: async (isWorking) => {
      const response = await axios.post("/clock/create");
      if (!response.data.success) {
        alert(isWorking ? "Clock Out failed!" : "Clock in failed!");
      } else {
        alert("clock " + (isWorking ? "out" : "in") + " successful!");
      }
    },
    checkWorking: async () => {
      const response = await axios.get("/clock/checkWorking");
      return response.data.success;
    },
  };
}
