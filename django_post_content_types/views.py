from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
import json
import xml.etree.ElementTree as ET
from .forms import MultipartForm


@ensure_csrf_cookie
def index(request):
    """Render the main page with all POST format examples"""
    return render(request, "index.html")


@require_http_methods(["POST"])
def handle_json(request):
    """Handle application/json requests"""
    try:
        data = json.loads(request.body)
        return JsonResponse(
            {
                "status": "success",
                "received": data,
                "content_type": request.content_type,
            }
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@require_http_methods(["POST"])
def handle_multipart(request):
    """Handle multipart/form-data requests (forms with files)"""
    form = MultipartForm(request.POST, request.FILES)

    if not form.is_valid():
        return JsonResponse(
            {
                "status": "error",
                "errors": form.errors,
                "content_type": request.content_type,
            },
            status=400,
        )

    form_data = {}

    for key, value in form.cleaned_data.items():
        if hasattr(value, "read"):
            form_data[key] = {
                "name": value.name,
                "size": value.size,
                "content_type": value.content_type,
            }
        else:
            form_data[key] = value

    return JsonResponse(
        {
            "status": "success",
            "form_data": form_data,
            "content_type": request.content_type,
        }
    )


@require_http_methods(["POST"])
def handle_urlencoded(request):
    """Handle application/x-www-form-urlencoded requests"""
    return JsonResponse(
        {
            "status": "success",
            "received": dict(request.POST),
            "content_type": request.content_type,
        }
    )


@require_http_methods(["POST"])
def handle_text_plain(request):
    """Handle text/plain requests"""
    text_content = request.body.decode("utf-8")
    return JsonResponse(
        {
            "status": "success",
            "received": text_content,
            "length": len(text_content),
            "content_type": request.content_type,
        }
    )


@require_http_methods(["POST"])
def handle_binary(request):
    """Handle application/octet-stream requests (raw binary data)"""
    binary_data = request.body
    return JsonResponse(
        {
            "status": "success",
            "size": len(binary_data),
            "content_type": request.content_type,
            "first_bytes": list(binary_data[:10]),
        }
    )


@require_http_methods(["POST"])
def handle_xml(request):
    """Handle application/xml requests"""
    try:
        xml_content = request.body.decode("utf-8")
        root = ET.fromstring(xml_content)

        data = {child.tag: child.text for child in root}

        return JsonResponse(
            {
                "status": "success",
                "root_tag": root.tag,
                "data": data,
                "content_type": request.content_type,
            }
        )
    except ET.ParseError:
        return JsonResponse({"error": "Invalid XML"}, status=400)


@require_http_methods(["POST"])
def handle_html(request):
    """Handle text/html requests"""
    html_content = request.body.decode("utf-8")
    return JsonResponse(
        {
            "status": "success",
            "received": html_content,
            "length": len(html_content),
            "content_type": request.content_type,
        }
    )


@require_http_methods(["POST"])
def handle_svg(request):
    """Handle image/svg+xml requests"""
    svg_content = request.body.decode("utf-8")
    return JsonResponse(
        {
            "status": "success",
            "received": svg_content,
            "length": len(svg_content),
            "content_type": request.content_type,
        }
    )


@require_http_methods(["POST"])
def handle_ndjson(request):
    """Handle application/x-ndjson requests"""
    try:
        ndjson_content = request.body.decode("utf-8")
        lines = [
            json.loads(line) for line in ndjson_content.strip().split("\n") if line
        ]

        return JsonResponse(
            {
                "status": "success",
                "lines_count": len(lines),
                "data": lines,
                "content_type": request.content_type,
            }
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid NDJSON"}, status=400)
