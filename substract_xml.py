base = """
<Property>Live.Device.Device._live_ptr<Description>Property</Description></Property>

<Property>Live.Device.Device.can_have_chains<Description>Property</Description></Property>

<Doc>	Returns true if the device is a rack.</Doc>

<Property>Live.Device.Device.can_have_drum_pads<Description>Property</Description></Property>

<Doc>	Returns true if the device is a drum rack.</Doc>

<Property>Live.Device.Device.canonical_parent<Description>Property</Description></Property>

<Doc>	Get the canonical parent of the Device.</Doc>

<Property>Live.Device.Device.class_display_name<Description>Property</Description></Property>

<Doc>	Return const access to the name of the device's class name as displayed in Live's browser and device chain</Doc>

<Property>Live.Device.Device.class_name<Description>Property</Description></Property>

<Doc>	Return const access to the name of the device's class.</Doc>

<Property>Live.Device.Device.is_active<Description>Property</Description></Property>

<Doc>	Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.</Doc>

<Property>Live.Device.Device.name<Description>Property</Description></Property>

<Doc>	Return access to the name of the device.</Doc>

<Property>Live.Device.Device.parameters<Description>Property</Description></Property>

<Doc>	Const access to the list of available automatable parameters for this device.</Doc>

<Property>Live.Device.Device.type<Description>Property</Description></Property>

<Doc>	Return the type of the device.</Doc>

<Property>Live.Device.Device.view<Description>Property</Description></Property>

<Doc>	Representing the view aspects of a device.</Doc>

<Method>Live.Device.Device.add_is_active_listener()<Description>Method</Description></Method>

<Doc>	add_is_active_listener( (Device)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "is_active" has changed. C++ signature :  void add_is_active_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.add_name_listener()<Description>Method</Description></Method>

<Doc>	add_name_listener( (Device)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "name" has changed. C++ signature :  void add_name_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.add_parameters_listener()<Description>Method</Description></Method>

<Doc>	add_parameters_listener( (Device)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "parameters" has changed. C++ signature :  void add_parameters_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.is_active_has_listener()<Description>Method</Description></Method>

<Doc>	is_active_has_listener( (Device)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "is_active". C++ signature :  bool is_active_has_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.name_has_listener()<Description>Method</Description></Method>

<Doc>	name_has_listener( (Device)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "name". C++ signature :  bool name_has_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.parameters_has_listener()<Description>Method</Description></Method>

<Doc>	parameters_has_listener( (Device)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "parameters". C++ signature :  bool parameters_has_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.remove_is_active_listener()<Description>Method</Description></Method>

<Doc>	remove_is_active_listener( (Device)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "is_active". C++ signature :  void remove_is_active_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.remove_name_listener()<Description>Method</Description></Method>

<Doc>	remove_name_listener( (Device)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "name". C++ signature :  void remove_name_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.remove_parameters_listener()<Description>Method</Description></Method>

<Doc>	remove_parameters_listener( (Device)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "parameters". C++ signature :  void remove_parameters_listener(TPyHandle&lt;ADevice&gt;,boost::python::api::object)</Doc>

<Method>Live.Device.Device.store_chosen_bank()<Description>Method</Description></Method>

<Doc>	store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -&gt; None : Set the selected bank in the device for persistency. C++ signature :  void store_chosen_bank(TPyHandle&lt;ADevice&gt;,int,int)</Doc>
""".split("\n")
extend = open("extract.xml", "r").read().split("\n")


def fetch_xml_elements(elements):
    properties = {}
    methods = {}
    for i, element in enumerate(elements):
        if element.startswith("<Property>"):
            if elements[i + 2].startswith("<Doc>"):
                doc = elements[i + 2].split("<Doc>	")[1].split("</Doc>")[0]
            else:
                doc = ""
            properties[element.split("<Property>")[1].split("<Description>")[0]] = doc
        elif element.startswith("<Method>"):
            if elements[i + 2].startswith("<Doc>"):
                doc = \
                    elements[i + 2].split("<Doc>	")[1].replace("-&gt;", "->").replace(" C++ signature", "").split("</Doc>")[
                        0]
            else:
                doc = ""
            methods[element.split("<Method>")[1].split("<Description>")[0]] = doc
    return properties, methods


device = fetch_xml_elements(base)
extended = fetch_xml_elements(extend)

device_stuff = [props.split(".")[-1] for props in device[0]] + [methods.split(".")[-1] for methods in device[1]]

for prop, desc in extended[0].items():
    if prop.split(".")[-1] not in device_stuff:
        print(prop, "|", desc)

for method, desc in extended[1].items():
    if method.split(".")[-1] not in device_stuff:
        print(method, "|", desc)
