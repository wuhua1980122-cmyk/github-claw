<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-brand">🎬 多媒体处理平台</div>
      <div class="nav-links">
        <router-link to="/">压缩</router-link>
        <router-link to="/convert">格式转换</router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>
<script>
export default { name: 'App' }
</script>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
.navbar{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:16px 32px;display:flex;justify-content:space-between;align-items:center}
.nav-brand{font-size:1.3em;font-weight:700}
.nav-links a{color:#fff;text-decoration:none;margin-left:20px;opacity:.8}
.nav-links a:hover{opacity:1;text-decoration:underline}
body{background:#f5f7fa;min-height:100vh}
</style>