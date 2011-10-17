/*jslint white: true, onevar: true, undef: true, nomen: false, eqeqeq: true, plusplus: true, bitwise: true, regexp: true, newcap: true, immed: true, strict: true */
/*global jQuery */
"use strict";

function FbLocales() {
    return (function ($) {
        var FALLBACK_LANGUAGE = 'en',

            languages = {},

            translate = function (text, lang) { // lang is optional
                var fbOptions, translation;
                if (!lang) {
                    // default value for language parameter
                    fbOptions = $($.fb.formbuilder.prototype.options._id).formbuilder('option');
                    // read ir from settings
                    lang = fbOptions.language;
                }
                if (languages.hasOwnProperty(lang)) {
                    // it's a valid language
                    translation = languages[lang][text];
                }
                if (!translation && translation !== '') { // must be string or undefined
                    if (FALLBACK_LANGUAGE === 'en') {
                        translation = text;
                    } else {
                        translation = languages[FALLBACK_LANGUAGE][text];
                    }
                }
                return translation;
            },

            addTranslation = function (lang, translations) {
                // translations must be an object
                var key;
                if (languages.hasOwnProperty(lang)) {
                    for (key in translations) {
                        if (translations.hasOwnProperty(key)) {
                            languages[lang] = translations[key];
                        }
                    }
                } else {
                    languages[lang] = translations;
                }
            };

        return {
            translate: translate,
            addTranslation: addTranslation
        };
    }(jQuery));
}
