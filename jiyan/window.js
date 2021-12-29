window = global;

window.sessionStorage = {
    // "tt_scid": "aVXi8etBnm.B58zyTc25..8dBzMZIeHLzrl.zXw8eVvS9yMsTRi5aBibvnpICYwq0ee3",
    removeItem: function (key) {
        delete this[key]
    },
    getItem: function (key) {
        return this[key] ? this[key]: null;
    },
    setItem: function (key, value) {
        this[key] = "" + value;  // 将数字转为字符串
    },
};

window.localStorage = {
        // ttcid: '89a06584eef94ed2bcf98a3c5996410f29',
        removeItem: function (key) {
            delete this[key]
        },
        getItem: function (key) {
            return this[key] ? this[key]: null;
        },
        setItem: function (key, value) {
            this[key] = "" + value;  // 将数字转为字符串
        },
};

window.OfflineAudioContext = function(){return {
    startRendering: function(){},
    renderedBuffer: {getChannelData: function () {return {slice: function () {return {reduce: function () {}}}}}},
    audioWorklet: {},
    currentTime: 0,
    destination: {channelCount: 1,
        channelCountMode: "explicit",
        channelInterpretation: "speakers",
        context: {oncomplete: null, length: 44100, destination: {}, currentTime: 0, sampleRate: 44100,},
        maxChannelCount: 1,
        numberOfInputs: 1,
        numberOfOutputs: 0},
    length: 44100,
    listener: {forwardX: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        forwardY: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        forwardZ: {value: -1, automationRate: 'a-rate', defaultValue: -1, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        positionX: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        positionY: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        positionZ: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        upX: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        upY: {value: 1, automationRate: 'a-rate', defaultValue: 1, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38},
        upZ: {value: 0, automationRate: 'a-rate', defaultValue: 0, minValue: -3.4028234663852886e+38, maxValue: 3.4028234663852886e+38}},
    oncomplete: null,
    onstatechange: null,
    sampleRate: 44100,
    state: "suspended",
    createOscillator: function () {
        return {
            channelCount: 2,
            channelCountMode: "max",
            channelInterpretation: "speakers",
            context: {audioWorklet: {},
                currentTime: 0,
                destination: {maxChannelCount: 1, context: {}, numberOfInputs: 1, numberOfOutputs: 0, channelCount: 1},
                length: 44100,
                listener: {positionX: {}, positionY: {}, positionZ: {}, forwardX: {}, forwardY: {},},
                oncomplete: null,
                onstatechange: null,
                sampleRate: 44100,
                state: "suspended"},
            detune: {automationRate: "a-rate",
                defaultValue: 0,
                maxValue: 153600,
                minValue: -153600,
                value: 0},
            frequency: {automationRate: "a-rate",
                defaultValue: 440,
                maxValue: 22050,
                minValue: -22050,
                value: 440,
                setValueAtTime: function () {}},
            numberOfInputs: 0,
            numberOfOutputs: 1,
            onended: null,
            type: "sine",
            connect: function () {},
            start: function () {},
        }},
    createDynamicsCompressor: function () {
        return {attack: {value: 0.003000000026077032, automationRate: 'k-rate', defaultValue: 0.003000000026077032, minValue: 0, maxValue: 1},
                channelCount: 2,
                channelCountMode: "clamped-max",
                channelInterpretation: "speakers",
                context: {oncomplete: null, length: 44100, destination: {}, currentTime: 0, sampleRate: 44100},
                knee: {value: 30, automationRate: 'k-rate', defaultValue: 30, minValue: 0, maxValue: 40},
                numberOfInputs: 1,
                numberOfOutputs: 1,
                ratio: {value: 12, automationRate: 'k-rate', defaultValue: 12, minValue: 1, maxValue: 20},
                reduction: 0,
                release: {value: 0.25, automationRate: 'k-rate', defaultValue: 0.25, minValue: 0, maxValue: 1},
                threshold: {automationRate: "k-rate", defaultValue: -24, maxValue: 0, minValue: -100, value: -24,
                setValueAtTime: function () {}},
                destination: {},
                startRendering: function () {},
                oncomplete: function () {},
                connect: function () {},
        }
    },
}};
window.indexedDB = {};
window.openDatabase = function(){};

plugins_base = {
        0: {description: "Portable Document Format", enabledPlugin: [], suffixes: "pdf", type: "application/pdf"},
        1: {description: "Portable Document Format", enabledPlugin: [], suffixes: "pdf", type: "text/pdf"},
        "application/pdf": {},
        "text/pdf": {},
        description: "Portable Document Format",
        filename: "internal-pdf-viewer",
        length: 2,
    };

var plugins = [
    Object.assign(plugins_base,{name: "PDF Viewer"}),
    Object.assign(plugins_base,{name: "Chrome PDF Viewer"}),
    Object.assign(plugins_base,{name: "Chromium PDF Viewer"}),
    Object.assign(plugins_base,{name: "Microsoft Edge PDF Viewer"}),
    Object.assign(plugins_base,{name: "WebKit built-in PDF"}),
];


var Navigator = function(){};
Navigator.prototype = {
    language: 'zh-CN',
    hardwareConcurrency: 12,
    appName: 'Netscape',
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    plugins: plugins,
    productSub: '20030107',
    languages: ['zh-CN', 'zh', 'zh-TW'],
    platform: 'Win32',
    maxTouchPoints: 0,
    deviceMemory: 8,
};

var Screen = function(){};
Screen.prototype = {
        availHeight: 1040,
        availLeft: 0,
        availTop: 0,
        availWidth: 1920,
        colorDepth: 24,
        height: 1080,
        pixelDepth: 24,
        width: 1920,
    };

CanvasRenderingContext2D = {
    rect: function () {},
    isPointInPath: function () {return false},
    fillRect: function () {},
    fillText: function () {},
    beginPath: function () {},
    arc: function () {},
    closePath: function () {},
    fill: function () {},
};
WebGLRenderingContext = {
    ARRAY_BUFFER: 34962,
    STATIC_DRAW: 35044,
    VERTEX_SHADER: 35633,
    FRAGMENT_SHADER: 35632,
    TRIANGLE_STRIP: 5,
    ALIASED_LINE_WIDTH_RANGE: 33902,
    DEPTH_TEST: 2929,
    LEQUAL: 515,
    COLOR_BUFFER_BIT: 16384,
    DEPTH_BUFFER_BIT: 256,
    ALIASED_POINT_SIZE_RANGE: 33901,
    ALPHA_BITS: 3413,
    BLUE_BITS: 3412,
    DEPTH_BITS: 3414,
    GREEN_BITS: 3411,
    MAX_COMBINED_TEXTURE_IMAGE_UNITS: 35661,
    MAX_CUBE_MAP_TEXTURE_SIZE: 34076,
    MAX_FRAGMENT_UNIFORM_VECTORS: 36349,
    MAX_RENDERBUFFER_SIZE: 34024,
    MAX_TEXTURE_IMAGE_UNITS: 34930,
    MAX_TEXTURE_SIZE: 3379,
    MAX_VARYING_VECTORS: 36348,
    MAX_VERTEX_ATTRIBS: 34921,
    MAX_VERTEX_TEXTURE_IMAGE_UNITS: 35660,
    MAX_VERTEX_UNIFORM_VECTORS: 36347,
    MAX_VIEWPORT_DIMS: 3386,
    RED_BITS: 3410,
    RENDERER: 7937,
    SHADING_LANGUAGE_VERSION: 35724,
    STENCIL_BITS: 3415,
    VENDOR: 7936,
    VERSION: 7938,
    HIGH_FLOAT: 36338,
    MEDIUM_FLOAT: 36337,
    LOW_FLOAT: 36336,
    HIGH_INT: 36341,
    MEDIUM_INT: 36340,
    LOW_INT:36339,
    createBuffer: function () {return {}},
    bindBuffer: function () {},
    bufferData: function () {},
    createProgram: function () {return {}},
    createShader: function () {return {}},
    shaderSource: function () {},
    compileShader: function () {},
    attachShader: function () {},
    linkProgram: function () {},
    useProgram: function () {},
    getAttribLocation: function () {return 0},
    getUniformLocation: function () {return {}},
    enableVertexAttribArray: function () {},
    vertexAttribPointer: function () {},
    uniform2f: function () {},
    drawArrays: function () {},
    clearColor: function () {},
    enable: function () {},
    depthFunc: function () {},
    clear: function () {},
    getExtension: function(name){
        if(name==='EXT_texture_filter_anisotropic') {
            return {MAX_TEXTURE_MAX_ANISOTROPY_EXT: 34047}
        }
        else if(name==='WEBGL_debug_renderer_info'){
            return {UNMASKED_VENDOR_WEBGL: 37445, UNMASKED_RENDERER_WEBGL: 37446}
        }
    },
    getParameter: function (pname) {
        pname_dict = {34047: 16, 33902: [1, 1], 33901: [1, 1024], 3413: 8, 3412: 8, 3411: 8, 3414: 24, 35661: 32,
        34076: 16384, 36349: 1024, 34024: 16384, 34930: 16, 3379: 16384, 36348: 30, 34921: 16, 35660: 16, 36347: 4096,
        3386: [32767, 32767], 3410: 8, 7937: 'WebKit WebGL', 35724: 'WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)',
        3415: 0, 7936: 'WebKit', 7938: 'WebGL 1.0 (OpenGL ES 2.0 Chromium)', 37445: 'Google Inc. (Intel)',
        37446: 'ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11-26.20.100.7463)'};
        return pname_dict[pname]
    },
    getContextAttributes: function () {return {antialias: true}},
    getShaderPrecisionFormat: function (shaderType, precisionType) {
        if (precisionType===36338 || precisionType===36337 || precisionType===36336){return {rangeMin: 127, rangeMax: 127, precision: 23}}
        else if (precisionType===36341 || precisionType===36340 || precisionType===36339){return {rangeMin: 31, rangeMax: 30, precision: 0}}
    },
    getSupportedExtensions: function () {return ['ANGLE_instanced_arrays', 'EXT_blend_minmax', 'EXT_color_buffer_half_float', 'EXT_disjoint_timer_query', 'EXT_float_blend', 'EXT_frag_depth', 'EXT_shader_texture_lod', 'EXT_texture_compression_bptc', 'EXT_texture_compression_rgtc', 'EXT_texture_filter_anisotropic', 'WEBKIT_EXT_texture_filter_anisotropic', 'EXT_sRGB', 'KHR_parallel_shader_compile', 'OES_element_index_uint', 'OES_fbo_render_mipmap', 'OES_standard_derivatives', 'OES_texture_float', 'OES_texture_float_linear', 'OES_texture_half_float', 'OES_texture_half_float_linear', 'OES_vertex_array_object', 'WEBGL_color_buffer_float', 'WEBGL_compressed_texture_s3tc', 'WEBKIT_WEBGL_compressed_texture_s3tc', 'WEBGL_compressed_texture_s3tc_srgb', 'WEBGL_debug_renderer_info', 'WEBGL_debug_shaders', 'WEBGL_depth_texture', 'WEBKIT_WEBGL_depth_texture', 'WEBGL_draw_buffers', 'WEBGL_lose_context', 'WEBKIT_WEBGL_lose_context', 'WEBGL_multi_draw']},
    canvas: {toDataURL: function () {
            return 'data:image/png;base64,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'
        }}

};
canvas = {
    getContext: function (contextType) {
        if (contextType==='2d'){
            return CanvasRenderingContext2D;
        }
        else if (contextType==='webgl'){
            return WebGLRenderingContext
        }
    },
    toDataURL: function () {
        return 'data:image/png;base64,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n3dh/jl/SmZevTNZ+Ez+sbj7LvO/NmneHJcrGUKAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECxQUmdUAvrusBBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFCNgIBezaksSoAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIlBQT0krpmEyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEA1AgJ6NaeyKAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiUFBDQS+qaTYAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQLVCAjo1ZzKogQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQUkBAL6lrNgECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAhUIyCgV3MqixIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBASQEBvaSu2QQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQjYCAXs2pLEqAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECJQUE9JK6ZhMgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBANQICejWnsigBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIlBQQ0Evqmk2AAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAEC1QgI6NWcyqIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUFJAQC+pazYBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIVCMgoFdzKosSIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQEkBAb2krtkECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUI2AgF7NqSxKgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAiUFBPSSumYTIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQDUCAno1p7IoAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECJQUENBL6ppNgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAtUICOjVnMqiBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFBSQEAvqWs2AQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECFQjIKBXcyqLEiBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEBJAQG9pK7ZBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFCNgIBezaksSoAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIlBQT0krpmEyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEA1AgJ6NaeyKAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiUFBDQS+qaTYAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQLVCAjo1ZzKogQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQUkBAL6lrNgECBAgQIECAAAEChz8tFQAAAwRJREFUBAgQIECAAAECBAgQIECAAAECBAhUIyCgV3MqixIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBASQEBvaSu2QQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQjYCAXs2pLEqAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECJQUE9JK6ZhMgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBANQICejWnsigBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIlBQQ0Evqmk2AAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAEC1QgI6NWcyqIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUFJAQC+pazYBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIVCMgoFdzKosSIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQEkBAb2krtkECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUI2AgF7NqSxKgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAiUFBPSSumYTIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQDUCAno1p7IoAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECJQUENBL6ppNgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAtUICOjVnMqiBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFBSQEAvqWs2AQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECFQjIKBXcyqLEiBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEBJAQG9pK7ZBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFCNgIBezaksSoAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIlBf4NC+onbY4yJZgAAAAASUVORK5CYII='
    },
    style: {display: 'inline'},
};

fontfamilys = ['Andale Mono', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial MT', 'Arial Narrow', 'Arial Rounded MT Bold', 'Arial Unicode MS', 'Bitstream Vera Sans Mono', 'Book Antiqua', 'Bookman Old Style', 'Calibri', 'Cambria', 'Cambria Math', 'Century', 'Century Gothic', 'Century Schoolbook', 'Comic Sans', 'Comic Sans MS', 'Consolas', 'Courier', 'Courier New', 'Geneva', 'Georgia', 'Helvetica', 'Helvetica Neue', 'Impact', 'Lucida Bright', 'Lucida Calligraphy', 'Lucida Console', 'Lucida Fax', 'LUCIDA GRANDE', 'Lucida Handwriting', 'Lucida Sans', 'Lucida Sans Typewriter', 'Lucida Sans Unicode', 'Microsoft Sans Serif', 'Monaco', 'Monotype Corsiva', 'MS Gothic', 'MS Outlook', 'MS PGothic', 'MS Reference Sans Serif', 'MS Sans Serif', 'MS Serif', 'MYRIAD', 'MYRIAD PRO', 'Palatino', 'Palatino Linotype', 'Segoe Print', 'Segoe Script', 'Segoe UI', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Symbol', 'Tahoma', 'Times', 'Times New Roman', 'Times New Roman PS', 'Trebuchet MS', 'Verdana', 'Wingdings', 'Wingdings 2', 'Wingdings 3']

CreateElementFun = function (Name) {
    offsetheight = [75];
    offsetwidth = [560, 530];
    Element = {
        tagName: Name.toUpperCase(),
        style: {},
        appendChild: function (u) {
        },
        removeChild: function () {},

        // 'offsetHeight': Math.round(Math.random()*70 + 20, 10),
        // 'offsetWidth': Math.round(Math.random()*400 + 400, 10),
        'offsetHeight': offsetheight[Math.floor(Math.random()*offsetheight.length)],
        'offsetWidth': offsetwidth[Math.floor(Math.random()*offsetwidth.length)],
    };
    Element.toString = function () {return '< ></ >'.replace(new RegExp(' ', 'g'), Name)};
    return Element
};


var Document = function(){};
Document.prototype = {
    createElement: function (tagName) {
        if (tagName==='canvas'){
            return canvas
        }
        else {
            return CreateElementFun(tagName)
        }
    },
    body: {
        appendChild: function () {},
        removeChild: function () {},
    },
    getElementsByClassName: function (calssNames) {return [{offsetHeight: 15, offsetLeft:1191, offsetWidth: 3, offsetTop: 461}]},
    getElementsByTagName: function (calssNames) {return [CreateElementFun(calssNames),]},
    '‌getElementById': function () {return {}},
};

var Location = function(){};
Location.prototype = {
        hash: "",
        host: "www.geetest.com",
        hostname: "www.geetest.com",
        href: "https://www.geetest.com/demo/slide-popup.html",
        origin: "https://www.geetest.com",
        pathname: "/",
        port: "",
        protocol: "https:",
        search: "",
    };

// document = new Document();
// navigator = new Navigator();
// screen = new Screen();
// window.WebGLRenderingContext = {};

module.exports = {
    window: window,
    document: function(){
        return new Document();},
    navigator: function(){
        return new Navigator();},
    screen: function(){
        return new Screen();},
    location: function () {
        return new Location();}
};
