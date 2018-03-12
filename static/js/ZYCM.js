var ZYCM = {
    getParam: function (a) { var b = location.search.substr(1, location.search.length), b = b.replace(/([\+])/g, " "), c = this.strToObj(decodeURIComponent(b)); return a ? c[a] : c },
    strToObj: function (a, b) { var e, f, g, c = [], d = {}; for (a = a.replace(/\?/g, "&"), c = a.split("&"), g = c.length, e = 0; g > e; e++) c[e].indexOf("=") < 0 || (f = c[e].split("="), d[f[0]] = b ? decodeURIComponent(f[1]) : f[1]); return d },
    objToStr: function (a, b) { var d, e, c = ""; for (d in a) "undefined" != typeof a[d] && (e = b ? encodeURIComponent(a[d]) : a[d], c += d + "=" + e + "&"); return c.slice(0, c.length - 1) },
    getHTML: function (id, data) { return txTpl(document.getElementById(id).innerHTML, data) },
    getFormatNumber: function (n) { var b = parseInt(n).toString(), len = b.length; if (len <= 3) { return b; } var r = len % 3; return r > 0 ? b.slice(0, r) + "," + b.slice(r, len).match(/\d{3}/g).join(",") : b.slice(r, len).match(/\d{3}/g).join(","); },
    getLocalStorage: function (key) { return localStorage.getItem(key) || (function (name) { var strCookie = document.cookie; var arrCookie = strCookie.split("; "); for (var i = 0; i < arrCookie.length; i++) { var arr = arrCookie[i].split("="); if (arr[0] == name) return unescape(arr[1]); } return null; })(key); },
    setLocalStorage: function (key, value) { localStorage.setItem(key, value); (function (name, value) { var cookieString = name + "=" + escape(value); var date = new Date(); date.setTime(date.getTime() + 365 * 24 * 3600 * 1000); cookieString = cookieString + "; expire=" + date.toGMTString(); document.cookie = cookieString; })(key, value); },
    getLocalPath: function () { var a = location.href, b = 0; return b = a.lastIndexOf("#"), b > 0 && (a = a.substring(0, b)), b = a.lastIndexOf("?"), b > 0 && (a = a.substring(0, b)), a },
    jsonToString: function (a) { var c, d, e, f, g, b = this; switch (typeof a) { case "string": return '"' + a.replace(/(["\\])/g, "\\$1") + '"'; case "array": return "[" + a.map(b.jsonToString).join(",") + "]"; case "object": if (a instanceof Array) { for (c = [], d = a.length, e = 0; d > e; e++) c.push(b.jsonToString(a[e])); return "[" + c.join(",") + "]" } if (null == a) return "null"; f = []; for (g in a) f.push(b.jsonToString(g) + ":" + b.jsonToString(a[g])); return "{" + f.join(",") + "}"; case "number": return a; case !1: return a } },
    stringToJSON: function (obj) { return eval("(" + obj + ")") },
    formatResultData: function (resultData) { if (typeof resultData == "string") { resultData = $.parseJSON(resultData); } return resultData; },
    //数组对象转为Json字符串
    stringify: function (arrObject) { return JSON.stringify(arrObject); }
};