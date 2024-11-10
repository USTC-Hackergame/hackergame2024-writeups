<!--
  - Copyright (c) 2024 ThrRip
  -
  - This Source Code Form is subject to the terms of the Mozilla Public
  - License, v. 2.0. If a copy of the MPL was not distributed with this
  - file, You can obtain one at https://mozilla.org/MPL/2.0/.
  -->

<template>
  <div class="flex flex-col gap-y-8 px-8 sm:px-12 xl:px-16 pt-4 py-8 lg:h-screen">
    <div class="flex max-xl:flex-col max-xl:gap-y-6 xl:justify-between">
      <h1 class="text-sm">
        "secret" decode
      </h1>
      <p class="text-sm">
        If you want a cool UI/UX/frontend like this for your project,
        feel free to reach out to me
        (<NuxtLink
          to="https://github.com/ThrRip"
          rel="noreferrer"
          target="_blank"
          class="font-bold underline"
        >ThrRip</NuxtLink>) 🤗
      </p>
    </div>
    <main
      class="grid grid-flow-row lg:grid-cols-2 lg:grid-rows-[auto_1fr] lg:grid-flow-col gap-x-12 gap-y-10 lg:h-full
      *:flex *:flex-col *:px-8 *:pb-8 *:border *:border-zinc-300"
    >
      <section>
        <h2 class="py-6 text-2xl font-bold">
          controls
        </h2>
        <div class="flex flex-col gap-y-8">
          <div class="flex flex-col gap-y-1">
            <p>
              Content area width:
              <input
                v-model.number="ctlContentAreaWidth"
                inputmode="numeric"
                size="4"
              >px
            </p>
            <p>
              Content area height:
              <input
                v-model.number="ctlContentAreaHeight"
                inputmode="numeric"
                size="4"
              >px
            </p>
            <p>
              Offset (X, Y) of the content area from the top left corner of the captured image:
              <input
                v-model.number="ctlContentAreaOffsetX"
                inputmode="numeric"
                size="4"
              >,
              <input
                v-model.number="ctlContentAreaOffsetY"
                inputmode="numeric"
                size="4"
              >
            </p>
            <p>
              Visual width
              (<span class="*:px-1 *:py-0.5 *:bg-zinc-900 *:font-mono">
                <span>_vw</span> in
                <span>encode_v.sh</span>
              </span>):
              <input
                v-model.number="ctlVisualWidth"
                inputmode="numeric"
                size="3"
              >
              columns
            </p>
            <p>
              Visual height
              (<span class="*:px-1 *:py-0.5 *:bg-zinc-900 *:font-mono">
                <span>_vh</span> in
                <span>encode_v.sh</span>
              </span>):
              <input
                v-model.number="ctlVisualHeight"
                inputmode="numeric"
                size="3"
              >
              lines
            </p>
            <p>
              (Optional) Start reading at
              <span class="px-1 py-0.5 bg-zinc-900 font-mono">
                {{ ctlReadStartAtMinute.toISOString().replace('00.000Z', '') }}<input
                  v-model.number="ctlReadStartAtSecond"
                  inputmode="numeric"
                  size="2"
                  class="bg-zinc-800"
                >.000Z
              </span>
            </p>
            <p>
              Read and decode every
              <input
                v-model.number="ctlReadEveryMs"
                inputmode="numeric"
                size="4"
              >ms
            </p>
            <p>
              (Optional) Stop after reading
              <input
                v-model.number="ctlStopAfterBytes"
                inputmode="numeric"
                size="6"
              >
              bytes
            </p>
          </div>
          <div class="grid grid-flow-col gap-x-6 h-14 *:border-2 *:border-zinc-200 hover:*:bg-zinc-900 active:*:bg-zinc-950">
            <button
              v-if="!ctlCapturing"
              @click="ctlStartCapture"
            >
              {{ ctlMsg ? ctlMsg : 'Start capture' }}
            </button>
            <button
              v-else
              @click="ctlStopCapture"
            >
              Stop capture
            </button>
          </div>
        </div>
      </section>
      <section>
        <h2 class="py-6 text-2xl font-bold">
          preview
        </h2>
        <div
          ref="viewVideoContainerEl"
          :class="{
            'max-lg:aspect-video grid place-items-center lg:h-full max-lg:max-h-56 border border-zinc-300': !ctlCapturing
          }"
        >
          <span v-if="!ctlCapturing">...</span>
          <video
            v-else
            ref="viewVideoEl"
            class="h-[--h]"
            :style="{ '--h': `${viewVideoHeight}px` }"
            @canplay="viewVideoEl?.play()"
          />
        </div>
      </section>
      <section class="row-span-2">
        <div class="flex justify-between items-baseline">
          <div class="flex max-xl:flex-col xl:gap-x-4 max-xl:gap-y-2 max-xl:py-6 items-baseline">
            <h2 class="xl:py-6 text-2xl font-bold">
              output
            </h2>
            <span>
              {{ outData.length }} chunks
              <template v-if="ctlCapturing">
                |
                {{
                  ctlCapturing ?
                    ctlReading ?
                      'Reading...' :
                      'Waiting to read...' :
                    ''
                }}
              </template>
            </span>
          </div>
          <button
            class="w-20 underline text-left"
            @click="outDataLive = !outDataLive"
          >
            Live: {{ outDataLive }}
          </button>
        </div>
        <div class="flex flex-col gap-y-6 lg:h-full">
          <textarea
            ref="outDataRenderedTextAreaEl"
            v-model="outDataRendered"
            :disabled="ctlReading"
            class="h-[28rem] lg:h-full font-mono whitespace-pre resize-none"
            @change="outDataUpdateFromRendered"
          />
          <div
            class="grid grid-cols-2 gap-x-6 h-14 *:grid *:place-items-center *:border-2 *:border-zinc-200
            hover:*:bg-zinc-900 active:*:bg-zinc-950 *:cursor-pointer"
          >
            <button @click="outDataClear">
              Clear
            </button>
            <a
              :href="outSaveURL"
              download="secret"
              @click="outSaveURLCreate"
            >
              Save
            </a>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
// controls
const ctlContentAreaWidth = ref<number>()
const ctlContentAreaHeight = ref<number>()
const ctlContentAreaOffsetX = ref<number>()
const ctlContentAreaOffsetY = ref<number>()
const ctlVisualWidth = ref<number>()
const ctlVisualHeight = ref<number>()
const ctlReadStartAtSecond = ref<number>()
const ctlReadEveryMs = ref<number>()
const ctlStopAfterBytes = ref<number>()

const ctlReadStartAtMinute = ref<Date>(new Date())
const ctlReadStartAtMinuteUpdateInterval = ref<ReturnType<typeof setInterval>>()
const ctlReadStartAt = computed<Date | 'now'>(() => {
  if (!ctlReadStartAtSecond.value || ctlReadStartAtSecond.value <= new Date().getSeconds()) return 'now'
  else return new Date(ctlReadStartAtMinute.value.getTime() + ctlReadStartAtSecond.value * 1000)
})
function ctlReadStartAtMinuteUpdate () {
  const newDate = new Date()
  newDate.setSeconds(0)
  newDate.setMilliseconds(0)
  ctlReadStartAtMinute.value = newDate
}
function ctlReadStartAtMinuteUpdateStart () {
  ctlReadStartAtMinuteUpdateInterval.value = setInterval(ctlReadStartAtMinuteUpdate, 1000)
}
ctlReadStartAtMinuteUpdate()
onMounted(ctlReadStartAtMinuteUpdateStart)

const ctlStopAfterChunksPixels = computed<[number, number] | false>(() => {
  if (!(ctlStopAfterBytes.value && ctlVisualWidth.value && ctlVisualHeight.value)) return false
  const chunks = Math.floor(ctlStopAfterBytes.value / (ctlVisualWidth.value * ctlVisualHeight.value / 8))
  const pixels = ctlStopAfterBytes.value % (ctlVisualWidth.value * ctlVisualHeight.value / 8) * 8
  return [chunks, pixels]
})

const ctlCapturing = ref(false)
const ctlReading = ref(false)
const ctlMsg = ref<string>()
const ctlMsgResetTimeout = ref<ReturnType<typeof setTimeout>>()

async function ctlStartCapture () {
  clearTimeout(ctlMsgResetTimeout.value)
  if (
    !ctlContentAreaWidth.value || ctlContentAreaWidth.value <= 0 ||
    !ctlContentAreaHeight.value || ctlContentAreaHeight.value <= 0 ||
    typeof ctlContentAreaOffsetX.value !== 'number' || ctlContentAreaOffsetX.value < 0 ||
    typeof ctlContentAreaOffsetY.value !== 'number' || ctlContentAreaOffsetY.value < 0 ||
    !ctlVisualWidth.value || ctlVisualWidth.value <= 0 ||
    !ctlVisualHeight.value || ctlVisualHeight.value <= 0 ||
    (
      typeof ctlReadStartAtSecond.value !== 'number' &&
      ctlReadStartAtSecond.value !== undefined &&
      ctlReadStartAtSecond.value !== ''
    ) ||
    (typeof ctlReadStartAtSecond.value === 'number' && ctlReadStartAtSecond.value < 0 && 59 < ctlReadStartAtSecond.value) ||
    typeof ctlReadEveryMs.value !== 'number' || ctlReadEveryMs.value < 0 ||
    (
      typeof ctlStopAfterBytes.value !== 'number' &&
      ctlStopAfterBytes.value !== undefined &&
      ctlStopAfterBytes.value !== ''
    ) ||
    (typeof ctlStopAfterBytes.value === 'number' && ctlStopAfterBytes.value <= 0)
  ) {
    ctlMsg.value = 'Please fill in all required control fields with valid values'
    ctlMsgResetTimeout.value = setTimeout(() => ctlMsg.value = undefined, 3000)
    return
  }
  else ctlMsg.value = undefined
  if (viewVideoContainerEl.value) {
    viewVideoHeight.value = viewVideoContainerEl.value.offsetHeight
    ctlCapturing.value = true
  }
  else return
  try {
    viewStream.value = await navigator.mediaDevices.getDisplayMedia({
      video: { displaySurface: 'browser' },
      // @ts-expect-error
      monitorTypeSurfaces: 'include',
      preferCurrentTab: false,
      selfBrowserSurface: 'exclude',
      surfaceSwitching: 'include',
      systemAudio: 'exclude'
    })
    await nextTick()
    if (viewVideoEl.value) viewVideoEl.value.srcObject = viewStream.value
    else ctlCapturing.value = false

    outReadCanvasCtx.value = new OffscreenCanvas(ctlContentAreaWidth.value, ctlContentAreaHeight.value).getContext('2d')
    for (let line = 1; line <= ctlVisualHeight.value; line++) {
      const lineY = Math.round(ctlContentAreaHeight.value / ctlVisualHeight.value * (0.5 + line - 1))
      for (let column = 1; column <= ctlVisualWidth.value; column++) {
        const columnX = Math.round(ctlContentAreaWidth.value / ctlVisualWidth.value * (0.5 + column - 1))
        outReadPixels.value?.push([columnX, lineY])
      }
    }

    if (ctlReadStartAt.value === 'now') outStartRead()
    else setTimeout(outStartRead, ctlReadStartAt.value.getTime() - new Date().getTime())
  }
  catch {
    ctlCapturing.value = false
  }
}
function ctlStopCapture () {
  outStopRead()
  viewStream.value?.getTracks().forEach(track => {
    track.stop()
  })
  ctlCapturing.value = false
}

// preview
const viewStream = ref<Awaited<ReturnType<typeof navigator.mediaDevices.getDisplayMedia>>>()
const viewVideoContainerEl = ref<HTMLDivElement>()
const viewVideoEl = ref<HTMLVideoElement>()
const viewVideoHeight = ref<number>(0)

// output
const outReadCanvasCtx = ref<OffscreenCanvasRenderingContext2D | null>()
const outReadPixels = ref<Array<[number, number]>>([])
const outReadFirstTimeout = ref<ReturnType<typeof setTimeout>>()
const outReadInterval = ref<ReturnType<typeof setInterval>>()
function outReadChunk () {
  let finalChunk = false
  let end = false
  if (
    ctlStopAfterChunksPixels.value !== false && (
      outData.value.length === ctlStopAfterChunksPixels.value[0] ||
      (ctlStopAfterChunksPixels.value[1] === 0 && outData.value.length === ctlStopAfterChunksPixels.value[0] - 1)
    )
  ) finalChunk = true
  outReadCanvasCtx.value?.drawImage(
    // @ts-expect-error
    viewVideoEl.value,
    ctlContentAreaOffsetX.value, ctlContentAreaOffsetY.value,
    ctlContentAreaWidth.value, ctlContentAreaHeight.value,
    0, 0,
    ctlContentAreaWidth.value, ctlContentAreaHeight.value
  )
  const chunk: Array<number> = []
  let byte = 0
  outReadPixels.value.forEach((pixel, index) => {
    if (end) return
    const pixelData = outReadCanvasCtx.value?.getImageData(pixel[0], pixel[1], 1, 1).data
    const bitIndex = 7 - index % 8
    if (
      Number(pixelData?.[0]) > 235 && Number(pixelData?.[1]) > 235 && Number(pixelData?.[2]) > 235
    ) byte += Math.pow(2, bitIndex)
    if (bitIndex === 0) {
      chunk.push(byte)
      byte = 0
    }
    if (
      finalChunk && ctlStopAfterChunksPixels.value !== false && (
        (ctlStopAfterChunksPixels.value[1] > 0 && index === ctlStopAfterChunksPixels.value[1] - 1) ||
        (ctlStopAfterChunksPixels.value[1] === 0 && index === outReadPixels.value.length - 1)
      )
    ) end = true
  })
  outData.value.push(chunk)
  if (outDataLive.value) outDataRenderedUpdate()
  if (end) ctlStopCapture()
}
function outStartRead () {
  outReadFirstTimeout.value = setTimeout(() => {
    ctlReading.value = true
    outReadChunk()
    outReadInterval.value = setInterval(outReadChunk, ctlReadEveryMs.value)
  // @ts-expect-error
  }, ctlReadEveryMs.value / 2)
}
function outStopRead () {
  clearTimeout(outReadFirstTimeout.value)
  clearInterval(outReadInterval.value)
  outReadPixels.value.length = 0
  outReadCanvasCtx.value = undefined
  ctlReading.value = false
  if (!outDataLive.value) outDataRenderedUpdate()
}

const outData = ref<Array<Array<number>>>([])
const outDataRendered = ref('[]')
const outDataRenderedTextAreaEl = ref<HTMLTextAreaElement>()
const outDataLive = ref(true)
async function outDataRenderedUpdate () {
  if (!outData.value.length) outDataRendered.value = '[]'
  else {
    let rendered = '[\n'
    outData.value.forEach((chunk, index) => {
      rendered += `  [${chunk.toString().replaceAll(',', ', ')}]`
      if (index === outData.value.length - 1) rendered += '\n'
      else rendered += ',\n'
    })
    rendered += ']'
    outDataRendered.value = rendered
  }
  if (ctlReading.value) {
    await nextTick()
    outDataRenderedTextAreaEl.value?.scroll(0, outDataRenderedTextAreaEl.value?.scrollHeight)
  }
}
function outDataUpdateFromRendered () {
  if (ctlReading.value) return
  const data: typeof outData['value'] = [];
  (JSON.parse(outDataRendered.value) as Array<Array<number>>).forEach(chunk => data.push(chunk))
  outData.value = data
  outDataRenderedUpdate()
}
function outDataClear () {
  outData.value.length = 0
  outDataRenderedUpdate()
}

const outSaveURL = ref<ReturnType<typeof URL['createObjectURL']>>()
function outSaveURLCreate () {
  outSaveURL.value = URL.createObjectURL(new Blob([new Uint8Array(outData.value.flat())]))
}
</script>
