<template>
  <div class="container">
    <h1>📦 文件压缩</h1>
    <p class="subtitle">支持图片、音频、视频压缩</p>
    <div class="upload-zone" @drop.prevent="handleDrop" @dragover.prevent @click="triggerUpload">
      <div class="upload-icon">📁</div>
      <p>拖拽文件到此处，或点击选择文件</p>
      <p class="hint">支持 jpg/png/gif/mp3/wav/mp4/avi</p>
      <input type="file" ref="fileInput" @change="handleFile" multiple hidden />
    </div>
    <div v-if="files.length" class="file-list">
      <div v-for="(f, i) in files" :key="i" class="file-item">
        <span>{{ f.name }}</span>
        <span :class="f.status">{{ f.statusMsg }}</span>
        <button v-if="f.resultUrl" @click="download(f)">⬇ 下载</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return { files: [] }
  },
  methods: {
    triggerUpload() { this.$refs.fileInput.click() },
    handleFile(e) {
      for (const f of e.target.files || []) this.addFile(f)
    },
    handleDrop(e) {
      for (const f of e.dataTransfer.files) this.addFile(f)
    },
    addFile(file) {
      const item = { name: file.name, file, status: 'pending', statusMsg: '等待处理', resultUrl: null }
      this.files.push(item)
      this.compress(item)
    },
    async compress(item) {
      item.status = 'processing'
      item.statusMsg = '压缩中...'
      const form = new FormData()
      form.append('file', item.file)
      try {
        const res = await fetch('/api/compress', { method: 'POST', body: form })
        if (!res.ok) throw new Error('压缩失败')
        const blob = await res.blob()
        item.resultUrl = URL.createObjectURL(blob)
        item.status = 'done'
        item.statusMsg = '✅ 压缩完成'
      } catch(e) {
        item.status = 'error'
        item.statusMsg = '❌ ' + e.message
      }
    },
    download(item) {
      const a = document.createElement('a')
      a.href = item.resultUrl; a.download = 'compressed_' + item.name; a.click()
    }
  }
}
</script>
<style scoped>
.container{max-width:800px;margin:40px auto;padding:0 20px}
h1{text-align:center;font-size:2em;margin-bottom:8px}
.subtitle{text-align:center;color:#888;margin-bottom:32px}
.upload-zone{border:2px dashed #ccc;border-radius:16px;padding:60px;text-align:center;cursor:pointer;transition:all .3s;background:#fff}
.upload-zone:hover{border-color:#667eea;background:#f8f9ff}
.upload-icon{font-size:3em;margin-bottom:12px}
.hint{color:#999;font-size:.85em;margin-top:8px}
.file-list{margin-top:24px}
.file-item{display:flex;align-items:center;gap:12px;padding:12px 16px;background:#fff;border-radius:8px;margin-bottom:8px;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.file-item span:first-child{flex:1}
.pending{color:#999}.processing{color:#f59e0b}.done{color:#10b981}.error{color:#ef4444}
button{padding:6px 16px;background:#667eea;color:#fff;border:none;border-radius:6px;cursor:pointer}
button:hover{background:#5a6fd6}
</style>