// Utility to get tg_id from Telegram WebApp JS API
export function getTelegramId() {
  if (
    window.Telegram &&
    window.Telegram.WebApp &&
    window.Telegram.WebApp.initDataUnsafe &&
    window.Telegram.WebApp.initDataUnsafe.user
  ) {
    return window.Telegram.WebApp.initDataUnsafe.user.id;
  }
  return "125364";
}

// Utility to get full Telegram user info
export function getTelegramUser() {
  if (
    window.Telegram &&
    window.Telegram.WebApp &&
    window.Telegram.WebApp.initDataUnsafe &&
    window.Telegram.WebApp.initDataUnsafe.user
  ) {
    const user = window.Telegram.WebApp.initDataUnsafe.user;
    return {
      tg_id: user.id,
      first_name: user.first_name,
      username: user.username || "string",
    };
  }
  // fallback for dev
  return {
    tg_id: "125364",
    first_name: "islom",
    username: "nigmatov",
  };
}
