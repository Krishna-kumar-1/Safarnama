package com.safarnama.app;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.webkit.GeolocationPermissions;
import android.webkit.PermissionRequest;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

public class MainActivity extends AppCompatActivity {

    private static final String PREFS_NAME = "SafarnamaPrefs";
    private static final String KEY_SERVER_URL = "server_url";
    private static final String DEFAULT_SERVER_URL = "http://10.0.2.2:5000"; // Android Emulator fallback
    private static final int PERMISSION_REQUEST_CODE = 101;

    private WebView webView;
    private ProgressBar progressBar;
    private SwipeRefreshLayout swipeRefreshLayout;
    private SharedPreferences prefs;

    private long lastBackPressTime = 0;
    private PermissionRequest currentAudioPermissionRequest;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        prefs = getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);

        progressBar = findViewById(R.id.progressBar);
        swipeRefreshLayout = findViewById(R.id.swipeRefreshLayout);
        webView = findViewById(R.id.webView);

        requestAppPermissions();
        configureWebView();

        swipeRefreshLayout.setColorSchemeColors(
            ContextCompat.getColor(this, R.color.primary_blue),
            ContextCompat.getColor(this, R.color.rail_orange)
        );
        swipeRefreshLayout.setOnRefreshListener(() -> webView.reload());

        loadApplication();
    }

    private void requestAppPermissions() {
        String[] permissions = new String[]{
            Manifest.permission.RECORD_AUDIO,
            Manifest.permission.ACCESS_FINE_LOCATION,
            Manifest.permission.ACCESS_COARSE_LOCATION
        };

        boolean needsRequest = false;
        for (String perm : permissions) {
            if (ContextCompat.checkSelfPermission(this, perm) != PackageManager.PERMISSION_GRANTED) {
                needsRequest = true;
                break;
            }
        }

        if (needsRequest) {
            ActivityCompat.requestPermissions(this, permissions, PERMISSION_REQUEST_CODE);
        }
    }

    @SuppressLint({"SetJavaScriptEnabled", "JavascriptInterface"})
    private void configureWebView() {
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setLoadsImagesAutomatically(true);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);
        settings.setBuiltInZoomControls(false);
        settings.setDisplayZoomControls(false);
        settings.setSupportZoom(false);
        settings.setMediaPlaybackRequiresUserGesture(false);

        // Optimization for low-end devices
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            settings.setSafeBrowsingEnabled(false);
        }
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);

        webView.setScrollBarStyle(View.SCROLLBARS_INSIDE_OVERLAY);
        webView.setOverScrollMode(View.OVER_SCROLL_NEVER);

        webView.setWebViewClient(new WebViewClient() {
            @Override
            public void onPageStarted(WebView view, String url, Bitmap favicon) {
                super.onPageStarted(view, url, favicon);
                progressBar.setVisibility(View.VISIBLE);
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);
                progressBar.setVisibility(View.GONE);
                swipeRefreshLayout.setRefreshing(false);
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                String url = request.getUrl().toString();
                if (url.startsWith("http://") || url.startsWith("https://") || url.startsWith("file:///")) {
                    return false; // Load inside WebView
                }
                // Handle tel, mailto, maps, external intents
                try {
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                    startActivity(intent);
                } catch (Exception e) {
                    // Ignore invalid intents
                }
                return true;
            }

            @Override
            public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error) {
                super.onReceivedError(view, request, error);
                if (request.isForMainFrame()) {
                    showErrorOrFallback();
                }
            }
        });

        webView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onProgressChanged(WebView view, int newProgress) {
                progressBar.setProgress(newProgress);
                if (newProgress == 100) {
                    progressBar.setVisibility(View.GONE);
                }
            }

            // Web Speech API / Microphone permission request in WebView
            @Override
            public void onPermissionRequest(PermissionRequest request) {
                String[] resources = request.getResources();
                for (String resource : resources) {
                    if (PermissionRequest.RESOURCE_AUDIO_CAPTURE.equals(resource)) {
                        if (ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.RECORD_AUDIO)
                                == PackageManager.PERMISSION_GRANTED) {
                            request.grant(new String[]{PermissionRequest.RESOURCE_AUDIO_CAPTURE});
                        } else {
                            currentAudioPermissionRequest = request;
                            ActivityCompat.requestPermissions(MainActivity.this,
                                new String[]{Manifest.permission.RECORD_AUDIO}, PERMISSION_REQUEST_CODE);
                        }
                        return;
                    }
                }
                request.grant(resources);
            }

            @Override
            public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
                callback.invoke(origin, true, false);
            }
        });
    }

    private void loadApplication() {
        String serverUrl = prefs.getString(KEY_SERVER_URL, "");
        if (serverUrl.isEmpty()) {
            // First try bundled local web assets, otherwise fallback to default server URL
            try {
                String[] assets = getAssets().list("www");
                if (assets != null && assets.length > 0) {
                    webView.loadUrl("file:///android_asset/www/index.html");
                    return;
                }
            } catch (Exception ignored) {
            }
            webView.loadUrl(DEFAULT_SERVER_URL);
        } else {
            webView.loadUrl(serverUrl);
        }
    }

    private void showErrorOrFallback() {
        // Try fallback to local bundled assets if online server was down
        try {
            String[] assets = getAssets().list("www");
            if (assets != null && assets.length > 0) {
                webView.loadUrl("file:///android_asset/www/index.html");
                Toast.makeText(this, "Operating in offline app mode", Toast.LENGTH_SHORT).show();
                return;
            }
        } catch (Exception ignored) {
        }

        // Show server configuration prompt so user can connect to their Codespace, LAN IP, or Cloud server
        new AlertDialog.Builder(this)
            .setTitle("Unable to connect to server")
            .setMessage("Could not connect to Safarnama server. Would you like to enter your backend server URL (e.g. from GitHub Codespaces or local WiFi)?")
            .setPositiveButton("Configure Server", (dialog, which) -> showServerConfigDialog())
            .setNegativeButton("Retry", (dialog, which) -> webView.reload())
            .setCancelable(false)
            .show();
    }

    public void showServerConfigDialog() {
        final EditText input = new EditText(this);
        input.setHint(R.string.server_url_hint);
        input.setText(prefs.getString(KEY_SERVER_URL, ""));

        new AlertDialog.Builder(this)
            .setTitle(R.string.server_url_dialog_title)
            .setView(input)
            .setPositiveButton("Connect", (dialog, which) -> {
                String url = input.getText().toString().trim();
                if (!url.startsWith("http://") && !url.startsWith("https://") && !url.isEmpty()) {
                    url = "http://" + url;
                }
                prefs.edit().putString(KEY_SERVER_URL, url).apply();
                Toast.makeText(this, "Saved server URL: " + url, Toast.LENGTH_SHORT).show();
                webView.loadUrl(url.isEmpty() ? DEFAULT_SERVER_URL : url);
            })
            .setNegativeButton("Reset to Local", (dialog, which) -> {
                prefs.edit().remove(KEY_SERVER_URL).apply();
                loadApplication();
            })
            .show();
    }

    @Override
    public void onBackPressed() {
        // First check if WebView or Leaflet map modal can close
        webView.evaluateJavascript(
            "(function() {" +
            "  var modal = document.querySelector('.modal-overlay.active');" +
            "  if (modal) { modal.classList.remove('active'); return true; }" +
            "  var aiModal = document.getElementById('aiChatOverlay');" +
            "  if (aiModal && aiModal.style.display !== 'none') { aiModal.style.display = 'none'; return true; }" +
            "  var mapCard = document.getElementById('mapCard');" +
            "  if (mapCard && mapCard.classList.contains('fullscreen-map')) { window.toggleMapFullscreen(); return true; }" +
            "  return false;" +
            "})();",
            value -> {
                if ("true".equals(value)) {
                    return; // JavaScript handled closing the overlay/modal!
                }
                if (webView.canGoBack()) {
                    webView.goBack();
                } else {
                    if (System.currentTimeMillis() - lastBackPressTime < 2000) {
                        super.onBackPressed();
                    } else {
                        lastBackPressTime = System.currentTimeMillis();
                        Toast.makeText(MainActivity.this, R.string.exit_prompt, Toast.LENGTH_SHORT).show();
                    }
                }
            }
        );
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == PERMISSION_REQUEST_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                if (currentAudioPermissionRequest != null) {
                    currentAudioPermissionRequest.grant(new String[]{PermissionRequest.RESOURCE_AUDIO_CAPTURE});
                    currentAudioPermissionRequest = null;
                }
            } else {
                if (currentAudioPermissionRequest != null) {
                    currentAudioPermissionRequest.deny();
                    currentAudioPermissionRequest = null;
                }
            }
        }
    }
}
