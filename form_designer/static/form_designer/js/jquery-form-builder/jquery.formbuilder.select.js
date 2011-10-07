/*
* JQuery Form Builder - Select field plugin.
*
* Revision: 1
* Version: 0.1
* Copyright 2011 Alejandro Blanco (ablanco@yaco.es)
*
* Licensed under Apache v2.0 http://www.apache.org/licenses/LICENSE-2.0.html
*
* Date: 30-Sep-2011
*/

var FbSelect = $.extend({}, $.fb.fbWidget.prototype, {
    options: { // default options. values are stored in widget's prototype
        name: 'Select',
        belongsTo: $.fb.formbuilder.prototype.options._standardFieldsPanel,
        _type: 'Select',
        _html: '<div><label><em></em><span></span></label> \
                <select class="select"></select> \
                <p class="formHint"></p></div>',
        _counterField: 'label',
        _languages: [ 'en' ],
        settings: {
            en: {
                label: 'Select',
                description: '',
                styles: {
                    fontFamily: 'default', // form builder default
                    fontSize: 'default',
                    fontStyles: [0, 0, 0] // bold, italic, underline
                }
            },
            required: false,
            readonly: false,
            options: [],
            styles: {
                label: {
                    color: 'default',
                    backgroundColor: 'default'
                },
                description: {
                    color: '777777',
                    backgroundColor: 'default'
                }
            }
        }
    },
    _init : function() {
        // calling base plugin init
        $.fb.fbWidget.prototype._init.call(this);
        // merge base plugin's options
        this.options = $.extend({}, $.fb.fbWidget.prototype.options, this.options);
    },
    _getWidget : function(event, fb) {
        var $jqueryObject = $(fb.target.options._html);
        fb.target._log('fbSelect._getWidget executing...');
        $('label span', $jqueryObject).text(fb.settings.label);
        if (fb._settings.required) {
            $('label em', $jqueryObject).text('*');
        }
        $('.formHint', $jqueryObject).text(fb.settings.description);
        fb.target._log('fbSelect._getWidget executed.');
        return $jqueryObject;
    },
    _getFieldSettingsLanguageSection : function(event, fb) {
        fb.target._log('fbSelect._getFieldSettingsLanguageSection executing...');
        var $label = fb.target._label({
            label: 'Label',
            name: 'field.label'
        }).append('<input type="text" id="field.label" />');
        $('input', $label).val(fb.settings.label).keyup(function(event) {
            var value = $(this).val();
            fb.item.find('label span').text(value);
            fb.settings.label = value;
            fb.target._updateSettings(fb.item);
        });
        var $name = fb.target._label({
            label: 'Name',
            name: 'field.name'
        }).append('<input type="text" id="field.name" />');
        $('input', $name).val(fb.item.find("input[id$='fields[" + fb.item.attr('rel') + "].name']").val()).keyup(function(event) {
            var value = $(this).val();
            fb.target._updateName(fb.item, value);
        });
        var $description = fb.target._label({
            label: 'Description',
            name: 'field.description'
        }).append('<textarea id="field.description" rows="2"></textarea>');
        $('textarea', $description).val(fb.settings.description).keyup(function(event) {
            var value = $(this).val();
            fb.item.find('.formHint').text(value);
            fb.settings.description = value;
            fb.target._updateSettings(fb.item);
        });
        var styles = fb.settings.styles;
        var fbStyles = fb.target._getFbLocalizedSettings().styles;
        var fontFamily = styles.fontFamily != 'default' ? styles.fontFamily : fbStyles.fontFamily;
        var fontSize = styles.fontSize != 'default' ? styles.fontSize : fbStyles.fontSize;
        var $fontPanel = fb.target._fontPanel({
            fontFamily: fontFamily,
            fontSize: fontSize,
            fontStyles: styles.fontStyles,
            idPrefix: 'field.',
            nofieldset: true
        });
        $("input[id$='field.bold']", $fontPanel).change(function(event) {
            if ($(this).attr('checked')) {
                fb.item.find('label').css('fontWeight', 'bold');
                fb.item.find('.select').css('fontWeight', 'bold');
                styles.fontStyles[0] = 1;
            } else {
                fb.item.find('label').css('fontWeight', 'normal');
                fb.item.find('.select').css('fontWeight', 'normal');
                styles.fontStyles[0] = 0;
            }
            fb.target._updateSettings(fb.item);
        });
        $("input[id$='field.italic']", $fontPanel).change(function(event) {
            if ($(this).attr('checked')) {
                fb.item.find('label').css('fontStyle', 'italic');
                fb.item.find('.select').css('fontStyle', 'italic');
                styles.fontStyles[1] = 1;
            } else {
                fb.item.find('label').css('fontStyle', 'normal');
                fb.item.find('.select').css('fontStyle', 'normal');
                styles.fontStyles[1] = 0;
            }
            fb.target._updateSettings(fb.item);
        });
        $("input[id$='field.underline']", $fontPanel).change(function(event) {
            if ($(this).attr('checked')) {
                fb.item.find('label span').css('textDecoration', 'underline');
                fb.item.find('.select').css('textDecoration', 'underline');
                styles.fontStyles[2] = 1;
            } else {
                fb.item.find('label span').css('textDecoration', 'none');
                fb.item.find('.select').css('textDecoration', 'none');
                styles.fontStyles[2] = 0;
            }
            fb.target._updateSettings(fb.item);
        });

        $("input[id$='field.fontFamily']", $fontPanel).change(function(event) {
            var value = $(this).val();
            fb.item.css('fontFamily', value);
            fb.item.find('.select').css('fontFamily', value);
            styles.fontFamily = value;
            fb.target._updateSettings(fb.item);
        });

        $("select[id$='field.fontSize']", $fontPanel).change(function(event) {
            var value = $(this).val();
            fb.item.find('label').css('fontSize', value + 'px');
            fb.item.find('.select').css('fontSize', value + 'px');
            styles.fontSize = value;
            fb.target._updateSettings(fb.item);
        });
        fb.target._log('fbSelect._getFieldSettingsLanguageSection executed.');
        return [fb.target._twoColumns($label, $name), fb.target._oneColumn($description), $fontPanel];
    },
    _getFieldSettingsGeneralSection : function(event, fb) {
        fb.target._log('fbSelect._getFieldSettingsGeneralSection executing...');
        var $required = $('<div><input type="checkbox" id="field.required" />&nbsp;Required</div>');
        var $readonly = $('<div><input type="checkbox" id="field.readonly" />&nbsp;Read-only</div>');
        var $valuePanel = fb.target._fieldset({
            text: 'Value'
        }).append(fb.target._oneColumn($required))
          .append(fb.target._oneColumn($readonly));
        $('input', $required).attr('checked', fb.settings.required).change(function(event) {
            if ($(this).attr('checked')) {
                fb.item.find('em').text('*');
                fb.settings.required = true;
            } else {
                fb.item.find('em').text('');
                fb.settings.required = false;
            }
            fb.target._updateSettings(fb.item);
        });

        $('input', $readonly).attr('checked', fb.settings.readonly).change(function(event) {
            if ($(this).attr('checked')) {
                fb.settings.readonly = true;
            } else {
                fb.settings.readonly = false;
            }
            fb.target._updateSettings(fb.item);
        });

        var $addOption = $('<div><label for="addOptionName">Name</label>&nbsp;<input id="addOptionName" type="text" />\
            <label for="addOptionValue">Value</label>&nbsp;<input id="addOptionValue" type="text" />\
            <span id="addOptionButton">Add option</span>\
            <div style="clear: both;"></div>\
            <span id="resetOptionsButton">Reset all options</span></div>');
        var $optionPanel = fb.target._fieldset({
            text: 'Options'
        }).append(fb.target._oneColumn($addOption));
        $('#addOptionButton', $addOption).css('cursor', 'pointer').css('float', 'right').css('text-decoration', 'underline').css('margin-top', '5px').click(function(event) {
            var fieldset = $(this.parentNode.parentNode),
                optionName = fieldset.find('#addOptionName'),
                optionValue = fieldset.find('#addOptionValue'),
                option, select;
            if (optionName[0].value !== '') {
                select = fb.item.find('select')[0];
                option = '<option value="' + optionValue[0].value + '">' + optionName[0].value + '</option>';
                fb.settings.options.push([optionName[0].value, optionValue[0].value]);
                optionValue[0].value = '';
                optionName[0].value = '';
                select.innerHTML += option;
                fb.target._updateSettings(fb.item);
            }
        });
        $('#resetOptionsButton', $addOption).css('cursor', 'pointer').css('float', 'right').css('text-decoration', 'underline').css('margin-top', '10px').click(function(event) {
            select = fb.item.find('select').text('');
            fb.settings.options = [];
            fb.target._updateSettings(fb.item);
        });

        var styles = fb.settings.styles;
        var $colorPanel = fb.target._labelValueDescriptionColorPanel(styles);

        $("input[id$='field.label.color']", $colorPanel).change(function(event) {
            var value = $(this).data('colorPicker').color;
            fb.item.css('color', '#' + value);
            styles.label.color = value;
            fb.target._updateSettings(fb.item);
        });

        $("input[id$='field.label.backgroundColor']", $colorPanel).change(function(event) {
            var value = $(this).data('colorPicker').color;
            fb.item.css('backgroundColor', '#' + value);
            styles.label.backgroundColor = value;
            fb.target._updateSettings(fb.item);
        });

        $("input[id$='field.description.color']", $colorPanel).change(function(event) {
            var value = $(this).data('colorPicker').color;
            fb.item.find('.formHint').css('color', '#' + value);
            styles.description.color = value;
            fb.target._updateSettings(fb.item);
        });

        $("input[id$='field.description.backgroundColor']", $colorPanel).change(function(event) {
            var value = $(this).data('colorPicker').color;
            fb.item.find('.formHint').css('backgroundColor', '#' + value);
            styles.description.backgroundColor = value;
            fb.target._updateSettings(fb.item);
        });
        fb.target._log('fbSelect._getFieldSettingsGeneralSection executed.');
        return [$valuePanel, $optionPanel, $colorPanel];
    },
    _languageChange : function(event, fb) {
        fb.target._log('fbSelect.languageChange executing...');
        var styles = fb.settings.styles;
        var fbStyles = fb.target._getFbLocalizedSettings().styles;
        var fontFamily = styles.fontFamily != 'default' ? styles.fontFamily : fbStyles.fontFamily;
        var fontSize = styles.fontSize != 'default' ? styles.fontSize : fbStyles.fontSize;
        var fontWeight = styles.fontStyles[0] == 1 ? 'bold' : 'normal';
        var fontStyle = styles.fontStyles[1] == 1 ? 'italic' : 'normal';
        var textDecoration = styles.fontStyles[2] == 1 ? 'underline' : 'none';

        fb.item.css('fontFamily', fontFamily);
        fb.item.find('label span').text(fb.settings.label).css('textDecoration', textDecoration);

        fb.item.find('label').css('fontWeight', fontWeight).css('fontStyle', fontStyle).css('fontSize', fontSize + 'px');

        fb.item.find('.select').val(fb.settings.value).css('fontWeight', fontWeight).css('fontStyle', fontStyle).css('textDecoration', textDecoration).css('fontFamily', fontFamily).css('fontSize', fontSize + 'px');

        fb.item.find('.formHint').text(fb.settings.description);
        fb.target._log('fbSelect.languageChange executed.');
    }
});

$.widget('fb.fbSelect', FbSelect);
